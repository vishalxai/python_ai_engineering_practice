# Q57 — AI Engineering: Token Counting with tiktoken
# You need to know how many tokens a prompt uses before sending it to an LLM.
#
# Write these functions:
#
# 1. count_tokens(text, model="gpt-4") → returns int token count using tiktoken
#
# 2. count_messages_tokens(messages, model="gpt-4")
#    → counts tokens for a list of {"role": ..., "content": ...} messages
#    → add 3 tokens per message for role/formatting overhead
#
# 3. fits_in_context(messages, model="gpt-4", max_tokens=8192) → bool
#    → returns True if the messages fit within the model's context window
#
# 4. trim_messages_to_fit(messages, model="gpt-4", max_tokens=4096)
#    → removes oldest messages (keep index 0 as system prompt always)
#    → until total tokens fit within max_tokens
#
# pip install tiktoken
