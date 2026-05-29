# Q55 — AI Engineering: Network Exceptions + Exponential Backoff
# Production LLM API calls fail. You need structured retry with backoff.
#
# Write a function call_llm_api(prompt) that:
#   - Makes a POST request to a mock endpoint
#   - Catches these specific exceptions separately:
#       requests.exceptions.Timeout      → log "Request timed out"
#       requests.exceptions.ConnectionError → log "Connection failed"
#       requests.exceptions.HTTPError    → log "HTTP error: {status_code}"
#   - Retries up to 3 times with exponential backoff: 1s, 2s, 4s between retries
#   - After 3 failures, raises a custom exception: LLMAPIError
#
# Write the custom exception class LLMAPIError(Exception) as well.
#
# import requests, time
# Exponential backoff formula: wait = base ** attempt  (base=2, attempt=0,1,2)
