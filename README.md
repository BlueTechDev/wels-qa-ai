# wels-qa-ai
Bible based ChatBot

# WELS QA AI Project

## Overview
The `wels-qa-ai` project aims to build an AI-powered question-answering system using data sourced from WELS topical Q&A content. The goal is to create vector embeddings for the data, leverage them for efficient content retrieval, and integrate an open-source LLM such as LLaMA to generate coherent responses based on user queries. 
The WELS QA AI project is an innovative tool designed to provide precise, context-aware answers to questions based on the WELS topical Q&A content. This project aims to enhance accessibility and understanding of faith-based topics through advanced AI technology.


## Project Structure
data/
Contains all data-related files, including:

Raw Data: Original JSONL files sourced from WELS Q&A content.
Processed Data: Cleaned and formatted data ready for embedding generation.
Vector Index Files: FAISS or similar indexes for performing fast similarity searches.
notebooks/
Jupyter notebooks used for experimenting, data preprocessing, and generating embeddings. These notebooks serve as a step-by-step guide to prepare the data for vector search.

src/
Python scripts for core project functionalities, including:

Embedding Generation: Scripts leveraging SentenceTransformers or similar models.
Vector Search: Code to perform similarity searches using FAISS or scikit-learn.
LLM Integration: Scripts to integrate and interact with large language models (e.g., LLaMA).
Main Application: The backend code for running the FastAPI-based chatbot application.
blog_posts/
Contains blog-style documentation of the project’s progress, key milestones, and technical insights. Each post is designed to document your journey and provide learning resources for others.

requirements.txt
A comprehensive list of Python dependencies required to run the project. This ensures consistency across environments and simplifies installation.

README.md
The primary project guide, including:

A detailed overview of the project and its goals.
Instructions for installation, setup, and running the application.
Links to relevant resources, including blog posts and external tools.

## Steps to Reproduce
Data Preparation:

Use the provided scripts or Jupyter notebooks in the notebooks/ folder to clean and preprocess the raw JSONL data.
Ensure consistency by handling missing values, removing duplicates, and standardizing the format for easy embedding generation.
Save the cleaned data as a new JSONL file in the data/processed/ directory.
Generate Embeddings:

Leverage sentence-transformers or a similar embedding model (e.g., SBERT or OpenAI’s embeddings) to convert textual data into vector representations.
Run the embedding generation script from the src/ folder:
bash
Copy code
python src/generate_embeddings.py --input data/processed/cleaned_data.jsonl --output data/vector_embeddings/embeddings.pkl  
Validate the embeddings by visualizing distances or clustering results using tools like t-SNE or PCA in notebooks/.
Vector Search Implementation:

Utilize FAISS for fast and efficient similarity search. Install it using:
bash
Copy code
pip install faiss-cpu  
Run the vector search script from the src/ folder to index and search embeddings:
bash
Copy code
python src/vector_search.py --input data/vector_embeddings/embeddings.pkl --query "Sample user query"  
Test retrieval accuracy by comparing search results to expected outputs using pre-defined test cases.
LLM Integration:

Integrate an open-source LLM like LLaMA or Hugging Face models to generate contextual responses based on retrieved results.
Update the API endpoint in the FastAPI backend to include:
Query embedding retrieval.
Passing the retrieved text as input to the LLM.
Example prompt for the LLM:
plaintext
Copy code
Context: [retrieved text]  
User Query: [user question]  
Response: Generate a relevant and coherent response based on the context.  
Deployment:

Use FastAPI to build and serve the chatbot. Install FastAPI and its dependencies:
bash
Copy code
pip install fastapi uvicorn  
Run the backend server locally:
bash
Copy code
uvicorn src.main:app --host 0.0.0.0 --port 8000  
For production, containerize the application using Docker and deploy it to a cloud platform like AWS or GCP:
Build the Docker image:
bash
Copy code
docker build -t wels-qa-ai .  
Deploy the container to your cloud infrastructure.

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
Phase 1: Current System (Completed by January 31)
Goal: Validate that the chatbot can retrieve relevant answers based on user queries using vector embeddings and a semantic search system.
Steps:

Finalize data preprocessing and embedding generation.
Test retrieval quality using SentenceTransformer with the embedded data (embedded_data.jsonl).
Deploy a basic FastAPI backend to handle user queries and return pre-existing responses.
Status: System ready for initial testing and validation.
Phase 2: Integrating Language Models for Dynamic Responses (February 1–29)
Objective: Enhance the chatbot to generate unique, conversational responses using an LLM (Large Language Model).
Steps:

Choose an LLM:

Evaluate and integrate an open-source LLM like LLaMA or GPT-based models.
Modify the FastAPI Endpoint:

Extend the backend to pass retrieved context from vector embeddings to the LLM.
Prompt Engineering:

Design prompts that instruct the LLM to use retrieved context to generate coherent, relevant responses.
Validation:

Test LLM responses for accuracy, coherence, and conversational flow using real sample queries.
Phase 3: Conversation Context Management (March 1–31)
Objective: Enable the chatbot to manage multi-turn conversations by remembering user interactions.
Steps:

Session Handling:

Implement session IDs or tokens to track and store user interactions.
Context Injection:

Pass user interaction history as part of the LLM prompt to maintain conversational context.
Memory Management:

Explore strategies for summarizing previous interactions to manage prompt length effectively.
Phase 4: Feedback and Iteration (April 1–15)
Objective: Refine the chatbot’s response quality based on user feedback and continuous iteration.
Steps:

Feedback Collection:

Develop a simple feedback mechanism where users can rate responses or flag issues.
Prompt Tuning:

Adjust the prompt structure based on common user feedback to optimize response relevance.
Fine-Tuning:

If necessary, fine-tune the LLM using custom data from the WELS Q&A corpus or user interactions.
Phase 5: Frontend Integration and User Interaction (April 16–30)
Objective: Create a user-friendly interface for real-time chatbot interactions.
Steps:

Web-Based UI:

Build a responsive web interface using React or Vue.js, connected to the FastAPI backend.
Mobile App Support (Optional):

Begin exploring mobile functionality with frameworks like React Native.
Testing:

Perform end-to-end testing with sample users to ensure smooth interactions.
Phase 6: Prototype Deployment and Scaling (May 1–15)
Objective: Prepare the chatbot for public testing and ensure scalability for a growing user base.
Steps:

Cloud Deployment:

Deploy the FastAPI app on a scalable cloud platform (AWS, Azure, or GCP).
Containerization:

Use Docker to containerize the application for consistent deployment environments.
Load Balancing:

Implement load balancers and auto-scaling features to manage traffic during public testing.
Public Testing:

Release the prototype to a small group of test users and collect detailed feedback.
