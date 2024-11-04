from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json

# Load data with embeddings
data_path = 'data/embedded_data.jsonl'
with open(data_path, 'r', encoding='utf-8') as infile:
    data = [json.loads(line) for line in infile]

# Extract embeddings and create an index
embeddings = np.array([entry['embedding'] for entry in data], dtype='float32')
index = faiss.IndexFlatL2(embeddings.shape[1])  # L2 is a standard metric for similarity search
index.add(embeddings)

# Load the pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# FastAPI setup
app = FastAPI()

class QueryRequest(BaseModel):
    query: str

def search(query_embedding, k=5):
    """Search the top k most similar entries."""
    distances, indices = index.search(np.array([query_embedding], dtype='float32'), k)
    results = [data[i] for i in indices[0]]
    return results

@app.post("/search/")
async def get_response(request: QueryRequest):
    """Handle user query and return full responses."""
    query_embedding = model.encode(request.query).tolist()
    results = search(query_embedding, k=5)  # Adjust `k` as needed

    if not results:
        raise HTTPException(status_code=404, detail="No results found")

    # Return the first complete response
    response = results[0]  # You can customize how many responses to return or format them
    return {
        "prompt": response['prompt'],
        "completion": response['completion']
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

