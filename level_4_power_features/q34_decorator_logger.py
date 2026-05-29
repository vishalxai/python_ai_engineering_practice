# Q34 — Power Features: Decorator (@log_calls)
# Write a decorator called log_calls that:
#   - Prints "Calling add with args=(2, 3) kwargs={}" before the function runs
#   - Prints "add returned 5" after it runs
#   - Works for any function, any arguments
#
# Apply it to:
# @log_calls
def add(a, b):
    return a + b

# This pattern is used heavily in production for debugging and observability.
