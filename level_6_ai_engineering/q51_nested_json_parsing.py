# Q51 — AI Engineering: Nested JSON Parsing
# Every LLM API returns deeply nested JSON. Practice extracting from it safely.
#
# Given this OpenAI-style response payload:
response = {
    "id": "chatcmpl-abc123",
    "object": "chat.completion",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "RAG stands for Retrieval Augmented Generation."
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 20,
        "completion_tokens": 10,
        "total_tokens": 30
    }
}
#
# Write a function extract_response(payload) that returns:
#   {"content": "...", "total_tokens": 30, "finish_reason": "stop"}
#
# Write a second function safe_extract(payload, *keys, default=None)
# that safely traverses any nested dict without crashing on missing keys.
# safe_extract(response, "choices", 0, "message", "content") → "RAG stands for..."
# safe_extract(response, "choices", 0, "delta", "content") → None  (missing key, no crash)
