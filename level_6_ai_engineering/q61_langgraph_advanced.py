# Q61 — AI Engineering: LangGraph Advanced — Multi-node + Conditional Edges
# Go beyond Q20. Build a real agentic workflow with branching logic.
#
# Build a research assistant graph:
#
# State:
#   question: str
#   needs_search: bool
#   search_results: list[str]
#   answer: str
#
# Nodes:
#   1. classify_node(state) → decides if question needs search (set needs_search)
#   2. search_node(state)   → fake search, adds results to state
#   3. answer_node(state)   → generates answer (with or without search results)
#
# Edges:
#   START → classify_node
#   classify_node → search_node   (if needs_search is True)
#   classify_node → answer_node   (if needs_search is False)
#   search_node   → answer_node
#   answer_node   → END
#
# This is a conditional edge — the graph branches based on state.
# from langgraph.graph import StateGraph, END
# from typing import TypedDict
