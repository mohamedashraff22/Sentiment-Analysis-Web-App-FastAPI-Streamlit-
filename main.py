from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Welcome to Sentiment Analysis API. Use /predict with POST."}


@app.post("/predict")
def predict_sentiment(input: InputText):
    analysis = TextBlob(input.text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return {"sentiment": sentiment, "polarity": polarity}
