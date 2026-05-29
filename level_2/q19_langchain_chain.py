# Q19 — LangChain: Prompt Template + LLM Chain
# Build a simple LangChain chain that answers questions.
#
# Steps:
#   1. Create a ChatPromptTemplate with a system message and a human message
#      System: "You are a helpful assistant."
#      Human:  "Answer this question: {question}"
#
#   2. Connect it to ChatOpenAI (or any LLM you have access to)
#
#   3. Add a StrOutputParser at the end
#
#   4. Invoke the chain with: {"question": "What is a vector database?"}
#      and print the result
#
# This is the LCEL (LangChain Expression Language) pattern — use the | pipe operator.
#
# Install: pip install langchain langchain-openai
