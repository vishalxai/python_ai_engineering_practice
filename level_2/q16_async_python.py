# Q16 — Async Python
# Write two async functions:
#   1. fetch_user()   — simulates a DB call, waits 1 second, returns {"id": 1, "name": "Vishal"}
#   2. fetch_orders() — simulates a DB call, waits 1 second, returns [{"item": "book"}, {"item": "pen"}]
#
# Then write a main() async function that runs BOTH calls in parallel (not one after the other)
# and prints the combined result.
#
# Key: total time should be ~1 second, not ~2 seconds.
# Hint: asyncio.gather()
#
# To run: python q16_async_python.py
