import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load data and model for embeddings
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
    """Handle user query and return an OpenAI-generated response based on context."""
    query_embedding = embedding_model.encode(request.query).tolist()
    results = search(query_embedding, k=1)

    if not results:
        raise HTTPException(status_code=404, detail="No results found")

    context = results[0]['completion']
    prompt_text = (
        f"Using the following information as context, respond to the question in a conversational way:\n\n"
        f"Context: {context}\n\n"
        f"User question: {request.query}\n\n"
        f"Response:"
    )

    try:
        # OpenAI API call with structured prompt and role-based messages
        chat_completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": "You are a friendly and knowledgeable assistant who provides thoughtful and accurate responses about faith."
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt_text
                        }
                    ]
                }
            ],
            max_tokens=150,
            temperature=0.7
        )

        # Extracting the response content correctly
        generated_response = chat_completion.choices[0].message.content.strip()

        return {
            "response": generated_response
        }

    except Exception as ex:
        print("OpenAI API error:", ex)
        raise HTTPException(status_code=500, detail="An error occurred with OpenAI's API")
