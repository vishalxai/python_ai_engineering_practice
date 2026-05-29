# Q53 — AI Engineering: Prompt Template Hydration
# In production, prompts are templates with variables injected at runtime.
#
# Given this template:
SYSTEM_PROMPT = """You are a helpful assistant for {company_name}.
Your tone is {tone}. You only answer questions about {topic}.
If asked about anything else, say: "{fallback_message}"
"""

RAG_PROMPT = """Context information:
{context}

---
User question: {question}

Answer based only on the context above. If the answer is not in the context, say "I don't know."
"""
#
# Write a function hydrate_prompt(template, **kwargs) that:
#   - Fills in all {variables} using the kwargs
#   - Raises ValueError with a clear message if a required variable is missing
#   - Raises ValueError if an unknown variable is passed (typo protection)
#
# Test with both prompts above.
