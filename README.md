# RAG-based Sales Chatbot

This project implements a Retrieval-Augmented Generation (RAG) based sales chatbot using MistralAI, LangChain, and Gradio. The chatbot is designed to answer queries about home appliances by retrieving relevant information from a vector store and generating responses using a large language model.

## Features

- Uses MistralAI's large language model for generating responses
- Implements RAG using FAISS vector store for efficient information retrieval
- Provides a user-friendly chat interface using Gradio

## Prerequisites

- Python 3.7+
- Required Python packages (install using `pip install -r requirements.txt`):
  - gradio
  - langchain
  - langchain_mistralai
  - faiss-cpu (or faiss-gpu for GPU support)

## Setup

1. Clone this repository
2. Install the required packages
3. Set up your MistralAI API key (replace `"rDjmdXGVUS37qMW2NOFP5vCpqlpve6Yt"` with your actual API key)
4. Prepare your vector store with relevant sales information (not included in this code)

## Usage

Run the main script:

```python
python chatbpt.py
```
