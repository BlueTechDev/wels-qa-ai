# wels-qa-ai
Bible based ChatBot

# WELS QA AI Project

## Overview
The `wels-qa-ai` project aims to build an AI-powered question-answering system using data sourced from WELS topical Q&A content. The goal is to create vector embeddings for the data, leverage them for efficient content retrieval, and integrate an open-source LLM such as LLaMA to generate coherent responses based on user queries.

## Project Structure
- **data/**: Contains raw data, processed data, and vector index files.
- **notebooks/**: Jupyter notebooks for data preprocessing and embedding generation.
- **src/**: Python scripts for generating embeddings, performing vector search, integrating with LLMs, and running the main application.
- **blog_posts/**: Blog-style documentation of our progress and key milestones.
- **requirements.txt**: List of Python dependencies required to run the project.
- **README.md**: This file, providing an overview and guidance for the project.

## Steps to Reproduce
1. **Data Preparation**:
   - Clean and structure the JSONL data for consistency.
2. **Generate Embeddings**:
   - Use `sentence-transformers` or a suitable embedding model to create vector embeddings for the data.
3. **Vector Search Implementation**:
   - Use `faiss` or `scikit-learn` for efficient similarity search.
4. **LLM Integration**:
   - Integrate an open-source LLM (e.g., LLaMA) for response generation.
5. **Deployment**:
   - Deploy the solution using FastAPI or Flask for interactive use.

## Getting Started
### Prerequisites
- Python 3.8+
- Recommended: Virtual environment for package isolation

### Installation
```bash
git clone https://github.com/yourusername/wels-qa-ai.git
cd wels-qa-ai
pip install -r requirements.txt

Future Roadmap: Building a Contextual AI Chat Agent
Phase 1: Current System (Initial Testing and Validation)
Goal: Validate that the chatbot can retrieve relevant answers based on user queries using vector embeddings and a semantic search system.
Status: The current setup with FastAPI and SentenceTransformer validates the ability to match user queries to relevant data entries in embedded_data.jsonl and return pre-existing responses.
Phase 2: Integrating Language Models for Dynamic Responses
Objective: Enhance the chatbot to generate unique, conversational responses using an LLM (Large Language Model).
Steps:
Choose an LLM: Integrate models like GPT, LLaMA, or other conversational models capable of natural language generation.
Modify the FastAPI Endpoint:
Extend the endpoint to pass the retrieved completion text as context to the LLM.
Craft a prompt structure that instructs the LLM to use the context to generate a new response.
Test LLM Integration:
Ensure that the model can generate responses that are relevant and conversational, and validate output quality.
Phase 3: Conversation Context Management
Objective: Enable the chatbot to remember previous user interactions and provide coherent responses over multi-turn conversations.
Steps:
Session Handling:
Implement session IDs or tokens to track user interactions.
Store conversation history temporarily during a user session.
Context Injection:
Pass conversation history as part of the LLM prompt to maintain context.
Memory Management:
Decide on a method for handling longer conversations, such as summarizing previous interactions to keep the prompt length manageable.
Phase 4: Feedback and Iteration
Objective: Refine the chatbot’s response quality through feedback and continuous improvements.
Steps:
User Feedback Collection:
Implement a feedback mechanism where users can rate responses or flag issues.
Prompt Tuning:
Adjust prompt engineering based on user feedback to optimize response generation.
Fine-Tuning:
Fine-tune the LLM on custom data if needed, using examples from your dataset and user interactions.
Phase 5: Frontend Integration and User Interaction
Objective: Develop or integrate a user-friendly interface for interacting with the chatbot in real-time.
Steps:
Web-Based UI:
Use frameworks like React or Vue.js for building a responsive web app.
Connect the frontend with your FastAPI backend to allow seamless user interaction.
Mobile App Integration:
Extend the functionality to mobile platforms using tools like React Native or Flutter.
Live Chat Embedding:
Integrate the chatbot with existing live chat platforms for broader use.
Phase 6: Deployment and Scaling
Objective: Prepare the chatbot for real-world usage with considerations for scalability and performance.
Steps:
Cloud Deployment:
Deploy the FastAPI app on cloud platforms like AWS, Azure, or Google Cloud.
Containerization:
Use Docker for containerizing the application to ensure consistency across different environments.
Load Balancing and Scaling:
Implement load balancers and auto-scaling to handle increased traffic as user base grows.
