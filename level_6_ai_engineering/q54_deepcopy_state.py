# Q54 — AI Engineering: Deep Copy vs Shallow Copy
# This is the #1 source of subtle bugs in LangGraph and stateful AI pipelines.
#
# Part 1 — understand the problem:
import copy

original = {"messages": ["hello", "world"], "metadata": {"count": 2}}

shallow = original.copy()         # or dict(original)
deep    = copy.deepcopy(original)

# Q: If you do shallow["messages"].append("new"), does original change? Why?
# Q: If you do deep["messages"].append("new"), does original change? Why?
# Write your answers as comments, then verify by running.

# Part 2 — the LangGraph pattern:
# In a graph node, you receive `state` as a dict.
# Write a function update_state(state, new_message) that:
#   - Does NOT mutate the input state
#   - Returns a NEW state dict with new_message appended to state["messages"]
#   - Uses deepcopy correctly
#
# This is exactly how LangGraph node functions must behave.
