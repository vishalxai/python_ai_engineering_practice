# Q17 — FastAPI: Pydantic + Dependency Injection
# Build a FastAPI app with the following:
#
# 1. A Pydantic model: UserQuery
#    Fields: query (str), top_k (int, default=3)
#
# 2. A dependency function: get_db()
#    For now, just return a fake dict: {"connected": True, "db": "postgres"}
#    (In real life this would return a DB session)
#
# 3. A POST endpoint: /search
#    - Accepts a UserQuery body
#    - Injects the get_db dependency
#    - Returns: {"query": ..., "top_k": ..., "db_status": ..., "results": []}
#
# To run: uvicorn q17_fastapi_advanced:app --reload
