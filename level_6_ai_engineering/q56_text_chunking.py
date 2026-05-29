# Q56 — AI Engineering: Text Chunking Strategies
# Chunking is the first step of every RAG pipeline. Know all three strategies.
#
# Given this long text (pretend it's a document):
text = """Artificial intelligence is transforming industries worldwide.
Machine learning models can now process vast amounts of data.
Natural language processing enables computers to understand human text.
Large language models like GPT have revolutionized text generation.
Retrieval augmented generation combines search with language models.
Vector databases store embeddings for fast similarity search.
"""
#
# Implement these three chunking functions:
#
# 1. chunk_fixed(text, chunk_size=100, overlap=20)
#    → splits by character count with overlap between chunks
#
# 2. chunk_by_sentences(text, sentences_per_chunk=2)
#    → splits into groups of N sentences
#
# 3. chunk_by_paragraphs(text)
#    → splits on double newlines (blank lines between paragraphs)
#
# Each function returns a list[str] of chunks.
# Print chunk count and first chunk for each strategy.
