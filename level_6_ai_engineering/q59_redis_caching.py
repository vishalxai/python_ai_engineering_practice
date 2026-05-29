# Q59 — AI Engineering: Redis Caching
# Cache LLM responses so identical queries don't hit the API twice.
# Redis is the standard tool for this in production AI systems.
#
# Write a cache layer for LLM responses:
#
# 1. cache_response(redis_client, query, response, ttl=3600)
#    → stores response with key = hash of query, expires after ttl seconds
#
# 2. get_cached_response(redis_client, query) → returns cached response or None
#
# 3. cached_llm_call(query) → decorator pattern:
#    - check cache first → return if hit
#    - call fake_llm(query) if miss → cache result → return
#
# 4. invalidate_cache(redis_client, query) → deletes the cached entry
#
# Use hashlib.md5 to hash the query string as the cache key.
#
# import redis, hashlib, json
# client = redis.Redis(host="localhost", port=6379, db=0)
# pip install redis
