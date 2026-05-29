# Q18 — RAG Pipeline (end-to-end skeleton)
# Build a simple RAG pipeline using ChromaDB + sentence-transformers (or OpenAI embeddings).
#
# Steps to implement:
#   1. INGEST: Take a list of text chunks, embed them, store in ChromaDB
#   2. RETRIEVE: Given a user query, embed it, find top-3 similar chunks from ChromaDB
#   3. GENERATE: Format a prompt with the retrieved chunks + query, print it
#              (no real LLM call needed — just show the final prompt string)
#
# Sample chunks to use:
chunks = [
    "RAG stands for Retrieval Augmented Generation.",
    "ChromaDB is an open-source vector database.",
    "LangChain helps build LLM-powered applications.",
    "Embeddings convert text into numerical vectors.",
    "FastAPI is a modern Python web framework.",
]
#
# Install: pip install chromadb sentence-transformers
