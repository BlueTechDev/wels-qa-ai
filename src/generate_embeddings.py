import json
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

# Load pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load JSONL data
input_path = 'data/raw_data.jsonl'
output_path = 'data/embedded_data.jsonl'

with open(input_path, 'r', encoding='utf-8') as infile:
    data = []
    for i, line in enumerate(infile, start=1):
        try:
            data.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON on line {i}: {e}")

# Generate embeddings with progress indication
for entry in tqdm(data, desc="Generating embeddings"):
    entry['embedding'] = model.encode(entry['completion']).tolist()

# Save the data with embeddings
with open(output_path, 'w', encoding='utf-8') as outfile:
    for entry in data:
        json.dump(entry, outfile)
        outfile.write("\n")

print("Embeddings generated and saved to 'embedded_data.jsonl'")
