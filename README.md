# 🧠 AI Text Summarizer

A full-stack AI application that generates concise summaries from long text using a fine-tuned Transformer (T5) model.

This project includes:

* ⚡ FastAPI backend
* 🎨 React frontend
* 🤗 Hugging Face model hosting
* 🐳 Docker for easy setup

---

## 🚀 Features

* AI-based text summarization
* Clean modern UI
* Word count & reduction stats
* Fully containerized (runs anywhere)

---

## 🛠 Tech Stack

* Frontend: React
* Backend: FastAPI
* Model: T5 (Transformers)
* Deployment: Docker

---

# 🚀 How to Run This Project (Step-by-Step)

Follow these steps carefully 👇

---

## ✅ Step 1: Install Docker

Download and install Docker Desktop:
👉 https://www.docker.com/products/docker-desktop/

After installing:

* Open Docker Desktop
* Make sure it is running

---

## ✅ Step 2: Create a folder

Create a new folder anywhere (for example Desktop):

```
Desktop/
 └── text-summarizer-run/
```

---

## ✅ Step 3: Create docker-compose.yml file

Inside that folder:

1. Right click → New File
2. Name it:

```
docker-compose.yml
```

---

## ✅ Step 4: Paste this inside the file

```yaml
version: "3.9"

services:
  backend:
    image: qudsi17/text-summary-backend:latest
    ports:
      - "8000:8000"

  frontend:
    image: qudsi17/text-summary-frontend:latest
    ports:
      - "3000:3000"
    depends_on:
      - backend
```

Save the file.

---

## ✅ Step 5: Open terminal in that folder

👉 IMPORTANT STEP

* Go to that folder
* Click on address bar
* Type:

```
cmd
```

* Press Enter

👉 Terminal will open in the same folder

---

## ✅ Step 6: Run the application

In terminal, run:

```bash
docker-compose up
```

---

## ⏳ First Run Note

* It may take **30–60 seconds**
* The model downloads from Hugging Face

---

## ✅ Step 7: Open the app

Open browser:

Frontend:

```
http://localhost:3000
```

Backend Docs:

```
http://localhost:8000/docs
```

---

# 🧪 Example Input

Paste this into the app:

```
Artificial Intelligence is transforming industries by automating processes, improving efficiency, and enabling better decision-making. However, it also raises concerns about job displacement and ethical issues such as bias and data privacy.
```

---

# 📈 Model Performance

* ROUGE-1: ~0.32
* ROUGE-2: ~0.13
* ROUGE-L: ~0.23

---

# 🧠 Model Details

* Fine-tuned on CNN/DailyMail dataset
* Hosted on Hugging Face

---

# 🌍 Deployment

This app can be deployed on:

* Render
* Railway
* AWS

---

# 👩‍💻 Author

**Qudsiya Siddique**

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub!
