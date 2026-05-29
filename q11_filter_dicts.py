# Q11 — Level 3: Functions and Real Patterns
# Write a function: filter_by_key(records, key, value)
# It takes a list of dicts and returns only the dicts where dict[key] == value.
#
# Example:
# records = [
#     {"name": "Alice", "role": "engineer"},
#     {"name": "Bob",   "role": "manager"},
#     {"name": "Carol", "role": "engineer"},
# ]
# filter_by_key(records, "role", "engineer")
# → [{"name": "Alice", "role": "engineer"}, {"name": "Carol", "role": "engineer"}]

def filter_by_key(records,key,value):
    result = []
    for record in records:
        if record[key] == value:
            result.append(record)
    return result

records = [
    {"name": "Alice", "role": "engineer"},
    {"name": "Bob",   "role": "manager"},
    {"name": "Carol", "role": "engineer"},
]

print(filter_by_key(records,"role","engineer"))
