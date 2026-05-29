# Q20 — LangGraph: State + Node + Simple Graph
# Build the simplest possible LangGraph workflow.
#
# Steps:
#   1. Define a State using TypedDict:
#      Fields: question (str), answer (str)
#
#   2. Write a node function: answer_node(state)
#      It reads state["question"], sets state["answer"] = "Answering: " + question
#      Returns the updated state
#
#   3. Build a StateGraph:
#      - Add the node
#      - Set it as the entry point
#      - Add an edge from the node to END
#      - Compile the graph
#
#   4. Invoke the graph with: {"question": "What is LangGraph?"}
#      Print the final state
#
# Install: pip install langgraph
