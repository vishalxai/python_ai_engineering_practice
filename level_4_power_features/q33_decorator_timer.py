# Q33 — Power Features: Decorator (@timer)
# Write a decorator called timer that:
#   - Records the time before and after a function runs
#   - Prints: "slow_function took 2.01s"
#   - Returns the original function's return value unchanged
#
# Apply it to this function:
import time

# @timer
def slow_function():
    time.sleep(1)
    return "done"

# Key: a decorator is a function that takes a function and returns a (wrapped) function.
# from functools import wraps  ← use this to preserve the original function's name
