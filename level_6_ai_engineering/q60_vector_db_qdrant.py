# Q60 — AI Engineering: Vector DB with Qdrant
# You already did ChromaDB in Q18. Now practice Qdrant — used more in production.
#
# Build a complete vector search pipeline:
#
# 1. Setup: create a Qdrant collection called "knowledge_base"
#    - vector size: 384 (sentence-transformers default)
#    - distance: Cosine
#
# 2. ingest(chunks: list[str]) → embed each chunk, store in Qdrant with metadata
#    - metadata: {"text": chunk, "chunk_id": i, "source": "manual"}
#
# 3. search(query: str, top_k=3) → embed query, return top_k similar chunks
#    - return list of {"text": ..., "score": ..., "chunk_id": ...}
#
# 4. delete_by_source(source: str) → delete all vectors with matching source metadata
#
# Use sentence-transformers for embeddings, qdrant-client for Qdrant.
# Run Qdrant locally with Docker: docker run -p 6333:6333 qdrant/qdrant
#
# pip install qdrant-client sentence-transformers
