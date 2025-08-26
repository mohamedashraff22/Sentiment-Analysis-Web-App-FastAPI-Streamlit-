# 🚀 Sentiment Analysis Web App (FastAPI + Streamlit)

A simple project that demonstrates how to build a **FastAPI backend** and connect it with a **Streamlit frontend**.
The app analyzes user input text and predicts whether the sentiment is **Positive, Negative, or Neutral**.

---

## 📂 Project Structure

```
sentiment-app/
├─ main.py        # FastAPI backend
├─ app.py         # Streamlit frontend
├─ requirements.txt
└─ README.md
```

---

## ⚙️ Setup & Installation

1. **Clone the repo (or create a new folder):**

   ```bash
   git clone https://github.com/yourusername/sentiment-app.git
   cd sentiment-app
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   conda create -n sentiment-app python=3.9
   conda activate sentiment-app
   ```

3. **Install dependencies:**

   ```bash
   pip install fastapi uvicorn textblob streamlit requests
   ```

   Also, download `textblob` corpora (first time only):

   ```bash
   python -m textblob.download_corpora
   ```

---

## ▶️ Running the App

### 1. Start FastAPI Backend

```bash
uvicorn main:app --reload --port 8000
```

* Server runs at: `http://127.0.0.1:8000`
* API Docs available at:

  * Swagger UI → `http://127.0.0.1:8000/docs`
  * ReDoc → `http://127.0.0.1:8000/redoc`

---

### 2. Start Streamlit Frontend

In a **new terminal**, run:

```bash
streamlit run app.py
```

* Streamlit UI runs at: `http://localhost:8501`

---

## 📌 Usage

1. Open the Streamlit app in your browser.
2. Enter a text (e.g., *"I love FastAPI, it’s awesome!"*).
3. Click **Analyze**.
4. The result shows:

   * Sentiment → Positive / Negative / Neutral
   * Polarity score (range: -1.0 → 1.0)

---

## 🛠 Example API Request (FastAPI directly)

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d "{\"text\": \"FastAPI is great!\"}"
```

Response:

```json
{
  "sentiment": "Positive",
  "polarity": 0.8
}
```

---

## 📖 Tech Stack

* **FastAPI** → backend API
* **Streamlit** → frontend UI
* **TextBlob** → sentiment analysis
* **Uvicorn** → ASGI server

---

## 👨‍💻 Author

Built by **Mohamed Ashraf** (learning FastAPI + Streamlit)
