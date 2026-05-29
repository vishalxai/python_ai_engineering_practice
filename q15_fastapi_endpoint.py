# Q15 — Level 3: Functions and Real Patterns
# Write a FastAPI app with one POST endpoint: /answer
# Request body:  { "query": "some question" }
# Response body: { "answer": "some answer" }
#
# Requirements:
# - Use Pydantic models for request and response
# - The endpoint should be async
# - For now, the "answer" can just echo back: "You asked: <query>"
#
# To run it (after writing): uvicorn q15_fastapi_endpoint:app --reload
