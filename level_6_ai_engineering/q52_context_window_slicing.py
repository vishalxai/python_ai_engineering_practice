# Q52 — AI Engineering: Context Window / Sliding Memory
# LLMs have token limits. You must trim conversation history to fit.
#
# Given a list of messages:
messages = [
    {"role": "user",      "content": "Hello"},
    {"role": "assistant", "content": "Hi! How can I help?"},
    {"role": "user",      "content": "What is RAG?"},
    {"role": "assistant", "content": "RAG is Retrieval Augmented Generation."},
    {"role": "user",      "content": "How does it work?"},
    {"role": "assistant", "content": "It retrieves relevant docs then generates an answer."},
    {"role": "user",      "content": "What vector DBs can I use?"},
]
#
# Write these functions:
#
# 1. keep_last_n(messages, n) → returns only the last n messages
#
# 2. trim_to_char_limit(messages, limit) → removes oldest messages until
#    total character count of all content is under the limit
#    Always keep at least the last 2 messages.
#
# 3. count_tokens_approx(messages) → approximate token count (1 token ≈ 4 chars)
#    Returns total estimated tokens for the message list
