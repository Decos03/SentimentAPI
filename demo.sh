# Start the server:
# uvicorn app:app --reload

# Run a couple of test requests:
curl -s -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "Tesla stock jumps after strong earnings"}' | jq

curl -s -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "Apple shares slide following weak iPhone sales"}' | jq
