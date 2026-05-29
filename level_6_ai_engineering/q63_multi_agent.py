# Q63 — AI Engineering: Multi-Agent Pattern
# Two agents collaborating: one researches, one writes.
#
# Build a two-agent pipeline using LangGraph:
#
# State:
#   topic: str
#   research_notes: str
#   draft: str
#   feedback: str
#   final: str
#   iteration: int
#
# Agents (nodes):
#   1. researcher_agent(state) → fills research_notes (fake: return 3 bullet points about topic)
#   2. writer_agent(state)     → writes a draft using research_notes
#   3. critic_agent(state)     → gives feedback on draft, sets feedback
#   4. revise_or_finish(state) → conditional: if iteration < 2, go back to writer; else go to END
#
# Edges:
#   START → researcher → writer → critic → revise_or_finish
#   revise_or_finish → writer (if iteration < 2)
#   revise_or_finish → END    (if iteration >= 2)
#
# This is the core pattern behind CrewAI and AutoGen.
