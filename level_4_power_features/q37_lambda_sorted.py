# Q37 — Power Features: Lambda + sorted()
# Given this list of dicts:
employees = [
    {"name": "Alice", "salary": 90000, "age": 30},
    {"name": "Bob",   "salary": 75000, "age": 25},
    {"name": "Carol", "salary": 95000, "age": 35},
    {"name": "Dave",  "salary": 75000, "age": 28},
]
#
# 1. Sort by salary (ascending)
# 2. Sort by salary descending, then by age ascending (multi-key sort)
# 3. Find the highest-paid employee using max()
#
# Use lambda as the key function: sorted(list, key=lambda x: x["field"])
