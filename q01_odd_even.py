# Q1 — Level 1: Syntax Muscle Memory
# Read a number from the user.
# Print "odd" if it is odd, "even" if it is even.


try:
    n = int(input("Enter a number: "))

    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
        print("Please enter a valid integer.")