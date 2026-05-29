# Q40 — Power Features: Advanced Comprehensions
# These are patterns you'll write constantly in AI engineering scripts.
#
# 1. Flatten a nested list using a comprehension (no loops):
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 2. From a list of strings, build a dict of {word: word_reversed} — one line:
words = ["hello", "python", "world"]

# 3. Given a list of dicts, extract just one field into a list — one line:
users = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
# Expected: ["Alice", "Bob"]

# 4. Set comprehension — unique first letters from a list of words:
animals = ["ant", "bear", "alligator", "bison", "cat"]
# Expected: {"a", "b", "c"}
