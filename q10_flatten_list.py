# Q10 — Level 2: Collections
# Given this nested list:
nested = [[1, 2], [3, 4], [5, 6]]
# Flatten it into a single list: [1, 2, 3, 4, 5, 6]
# Try to do it in one line.
result = []
for inner in nested:
    for item in inner:
        result.append(item)

print(result)

