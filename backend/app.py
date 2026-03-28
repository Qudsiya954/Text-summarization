from fastapi import FastAPI
from pydantic import BaseModel

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from fastapi.middleware.cors import CORSMiddleware
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

@app.get("/")
def home():
    return {"message": "Summarization API is running"}

@app.post("/summarize")
def summarize(req: TextRequest):
    inputs = tokenizer(
        "summarize: " + req.text,
        return_tensors="pt",
        max_length=128,
        truncation=True
    ).to(device)

    outputs = model.generate(
        inputs["input_ids"],
        max_length=60,
        num_beams=4
    )

    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"summary": summary}