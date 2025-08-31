from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_sentiment

app = FastAPI(
    title="Stock Sentiment API",
    description="Quick service for classifying financial headlines or tweets.",
    version="0.1"
)

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(request: InputText):
    """Classify a piece of text as positive or negative sentiment."""
    prediction = predict_sentiment(request.text)
    return {"text": request.text, "prediction": prediction}
