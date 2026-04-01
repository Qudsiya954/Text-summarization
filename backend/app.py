from fastapi import FastAPI
from pydantic import BaseModel

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from fastapi.middleware.cors import CORSMiddleware
from azure.data.tables import TableServiceClient
import uuid
from dotenv import load_dotenv
import os

load_dotenv()

connection_string = os.getenv("AZURE_CONN")

if not connection_string:
    raise ValueError("AZURE_CONN is not set!")
table_service = TableServiceClient.from_connection_string(conn_str=connection_string)

table_name = "summaries"

table_client = table_service.get_table_client(table_name=table_name)
app = FastAPI()

# Load model
MODEL_PATH = "Qudsiya17/t5-summarizer"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Request schema
class TextRequest(BaseModel):
    text: str

def generate_summary(text):
    input_text = "summarize: " + text

    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True).to(device)

    outputs = model.generate(
        inputs,
        max_length=150,
        min_length=30,
        num_beams=4,
        early_stopping=True
    )

    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary

@app.get("/")
def home():
    return {"message": "Summarization API is running"}

@app.post("/summarize")
async def summarize(data: TextRequest):
    text = data.text

    summary = generate_summary(text)

    entity = {
        "PartitionKey": "summary",
        "RowKey": str(uuid.uuid4()),
        "input_text": text,
        "summary_text": summary
    }
    print("Saving to Azure Table...")
    table_client.upsert_entity(entity=entity)
    print("Saved successfully!")

    return {"summary": summary}
