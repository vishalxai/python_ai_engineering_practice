# Q2 — Level 1: Syntax Muscle Memory
# Read a number from the user.
# Print "Fizz"     if divisible by 3
# Print "Buzz"     if divisible by 5
# Print "FizzBuzz" if divisible by both 3 and 5
# Print the number itself if none of the above

try:
    num = int(input("What's the number: "))

    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 ==0:
        print("Fizz")
    elif num % 5 ==0:
        print("Buzz")
    else:
        print(f"{num}")
    
except ValueError:
    print("This is not a valid number")
