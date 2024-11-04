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
