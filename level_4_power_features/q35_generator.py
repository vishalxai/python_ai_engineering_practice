# Q35 — Power Features: Generators (yield)
# Write a generator function fibonacci(n) that yields Fibonacci numbers up to n terms.
#
# Expected: list(fibonacci(7)) → [0, 1, 1, 2, 3, 5, 8]
#
# Key difference from a normal function:
#   - uses yield instead of return
#   - pauses execution and resumes where it left off on next()
#   - memory-efficient: doesn't build the whole list at once
#
# Also write a generator count_up(start, end) that yields numbers from start to end.
