# Q6 — Level 2: Collections
# Read 5 numbers from the user into a list.
# Print only the even numbers from that list.

num = list(map(int,input("write the 5 numbers with space").split()))
for n in num:
    if n % 2 == 0:
        print(n)