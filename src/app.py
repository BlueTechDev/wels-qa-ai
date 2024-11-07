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

# Print to confirm that the API key is being loaded
print("Loaded API Key:", os.getenv("OPENAI_API_KEY"))

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
    """Handle user query and return a biblically grounded, scripture-supported response."""
    query_embedding = embedding_model.encode(request.query).tolist()
    results = search(query_embedding, k=1)

    if not results:
        raise HTTPException(status_code=404, detail="No results found")

    # Adding context and crafting the prompt
    context = results[0]['completion']
    prompt_text = (
        f"Using the following context, answer in clear and conversational English. "
        f"Ensure the response is grammatically correct and natural-sounding. "
        f"Incorporate multiple relevant Bible passages where possible to support your answer."
        f"Answer in a compassionate, conversational tone, ensuring theological precision."
        f"clarify theological terms in simple language, helping users who may not be familiar with church-specific language"
        f"In your response, clarify any specific theological terms or concepts, such as 'blasphemy against the Holy Spirit,' explaining them in simple language for better understanding."
        f"Context: {context}\n\n"
        f"User question: {request.query}\n\n"
        f"Response:"
    )

    try:
        # OpenAI API call with structured prompt
        chat_completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
          "role": "system",
"content": [
    {
        "type": "text",
        "text": (
            "You are a knowledgeable assistant specializing in Christian theology. "
            "Answer all questions from a biblical perspective, using traditional Christian interpretations and incorporating relevant scripture to support your answers. "
            "Highlight that this resource provides supportive information and is not a substitute for personal guidance with a pastor or trusted church leader, especially on complex or deeply personal topics. "
            "Encourage users to engage in conversations with their church leaders for tailored advice and insights, complementing the information provided here. "
            
            "For topics foundational to Christian belief—such as the Trinity, God’s nature, creation, justification, and the Means of Grace—offer clear, respectful explanations. "
            "When explaining the Trinity, convey that God is one true, holy, eternal being, revealed as Father, Son, and Holy Spirit. These three persons are united as one God, equal in power and glory (Deuteronomy 6:4; Matthew 28:19; John 5:23). "
            "Explain that the Bible, inspired by the Holy Spirit, is God's true word, containing all necessary knowledge for salvation. Support this with passages such as 2 Timothy 3:16, 2 Peter 1:21, and John 5:39. "
            "Describe the special creation of humanity in God’s image (Genesis 1:26, Genesis 2:7), the fall into sin, and its consequences, using passages like Genesis 2:17, Psalm 51:5, and Ephesians 2:1. "
            "Emphasize that only through the work of the Holy Spirit, through the Word, can individuals come to faith (1 Corinthians 2:14). "
            
            "For the 'Means of Grace,' explain each part—God’s Word, Baptism, and Holy Communion—as unique ways God imparts His love, forgiveness, and presence. "
            "Illustrate that these means are how believers experience God’s grace directly, supported by verses like Romans 10:17, Acts 2:38, and Matthew 26:28. "
            
            "Explain justification by faith as central to salvation, with clarity and simplicity. State that God declared all sinners righteous through Jesus’ sacrifice, and this forgiveness is received by faith alone, as noted in Ephesians 2:8-9, Romans 3:22-24, and 2 Corinthians 5:19. "
            
            "Use simple language and avoid complex theological jargon when possible, especially for challenging topics like Communion as Jesus' body and blood. "
            "Include relevant Bible passages to support each point and provide concise explanations of how these passages relate to the topic, helping readers with diverse backgrounds understand. "
            
            "Maintain empathy in your responses, recognizing that many theological topics are deeply complex and may be difficult to grasp. "
            "Encourage thoughtful reflection, reminding users of God’s love and justice. "
            "All responses should be in grammatically correct and conversational English to ensure clarity and accessibility."
        )
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
    max_tokens=350,
    temperature=0.3  # Lower temperature for accuracy and consistency
)


        # Extracting the response content and cleaning it
        generated_response = (
        chat_completion.choices[0].message.content
        .strip()
        .replace("\\\"", "\"")       # Replace escaped double quotes with regular double quotes
        .replace("\\'", "'")         # Replace escaped single quotes with regular single quotes
        .replace("\\", "")           # Remove any remaining backslashes
        .replace("\n", " ")          # Replace newline characters with spaces for readability
        .replace("  ", " ")          # Replace any double spaces that might occur
    )

        return {
            "response": generated_response
        }

    except Exception as ex:
        print("OpenAI API error:", ex)
        raise HTTPException(status_code=500, detail="An error occurred with OpenAI's API")
