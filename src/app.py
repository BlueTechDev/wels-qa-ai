from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json

# Load the data and model for embeddings
data_path = 'data/embedded_data.jsonl'
with open(data_path, 'r', encoding='utf-8') as infile:
    data = [json.loads(line) for line in infile]

embeddings = np.array([entry['embedding'] for entry in data], dtype='float32')
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

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
    """Handle user query and return the most relevant context without LLM generation."""
    query_embedding = embedding_model.encode(request.query).tolist()
    results = search(query_embedding, k=1)

    if not results:
        raise HTTPException(status_code=404, detail="No results found")

    context = results[0]['completion']

    return {
        "prompt": results[0]['prompt'],
        "context": context
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
