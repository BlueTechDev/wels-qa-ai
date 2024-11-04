import faiss
import numpy as np
import json
from sentence_transformers import SentenceTransformer

# Load data with embeddings
data_path = 'data/embedded_data.jsonl'
with open(data_path, 'r', encoding='utf-8') as infile:
    data = [json.loads(line) for line in infile]

# Extract embeddings and create an index
embeddings = np.array([entry['embedding'] for entry in data], dtype='float32')
index = faiss.IndexFlatL2(embeddings.shape[1])  # L2 is a standard metric for similarity search
index.add(embeddings)

# Search function
def search(query_embedding, k=5):
    """Search the top k most similar entries."""
    distances, indices = index.search(np.array([query_embedding], dtype='float32'), k)
    results = [data[i] for i in indices[0]]
    return results

print("Vector search setup complete.")

# Test search function
model = SentenceTransformer('all-MiniLM-L6-v2')

def test_search(query, top_k=5):
    """Generate an embedding for a query and search for the most similar entries."""
    query_embedding = model.encode(query).tolist()
    results = search(query_embedding, k=top_k)
    
    # Print the search results
    print("\nTop results for your query:")
    for i, result in enumerate(results, start=1):
        print(f"\nResult {i}:")
        print(f"Prompt: {result['prompt']}")
        print(f"Completion: {result['completion'][:300]}...")  # Print the first 300 characters for brevity

# Run the test
if __name__ == "__main__":
    test_query = "baptism"  # Replace with your desired test query
    test_search(test_query)
