# Q62 — AI Engineering: Streaming LLM Responses
# Production AI apps stream responses token by token — never wait for the full response.
#
# Part 1 — Fake streaming (understand the pattern):
# Write a generator function stream_response(text) that:
#   - Takes a full text string
#   - Yields it word by word with a small delay (0.05s)
#   - Caller prints each word as it arrives (no newline, flush=True)
#
# Part 2 — FastAPI streaming endpoint:
# Write a GET /stream endpoint that:
#   - Accepts a query param: ?question=...
#   - Returns a StreamingResponse
#   - Streams the fake response word by word
#   - Content-type: text/event-stream (SSE format)
#
# Part 3 — OpenAI streaming (if you have an API key):
# Show how to use stream=True with the OpenAI client and iterate chunks.
#
# from fastapi import FastAPI
# from fastapi.responses import StreamingResponse
# import asyncio
