# Q9 — Level 2: Collections
# Given these two lists:
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
# Return (or print) the elements that appear in both lists.
# Expected output: [3, 4, 5]
list_c = list(set(list_a) & set(list_b))
print(list_c)
