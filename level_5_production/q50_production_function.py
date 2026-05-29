# Q50 — Production: Put It All Together
# Write a production-quality function that summarises a list of documents using an LLM.
# Use everything you've learned: type hints, logging, error handling, Pydantic, async.
#
# Function signature:
#   async def summarize_documents(docs: list[str], max_tokens: int = 500) -> SummaryResult
#
# SummaryResult (Pydantic model):
#   - summaries: list[str]
#   - total_docs: int
#   - failed: int
#
# Requirements:
#   - Type hints on everything
#   - Logger that logs each step (DEBUG/INFO/ERROR)
#   - Handle the case where a doc is empty (skip it, increment failed count)
#   - For now, fake the LLM call: return "Summary of: {doc[:50]}..."
#   - Use asyncio.gather to process all docs concurrently
#
# This is the pattern you'll write on day 1 at Rokkun.io.
