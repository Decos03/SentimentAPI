from transformers import pipeline

# Simple wrapper around a pre-trained sentiment model.
# Can be swapped for FinBERT or another finance-specific model later.
_sentiment = pipeline("sentiment-analysis")

def predict_sentiment(text: str):
    result = _sentiment(text)[0]
    return {
        "label": result["label"],
        "confidence": round(result["score"], 4)
    }
