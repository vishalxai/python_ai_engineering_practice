# Q25 — OOP: @classmethod and @staticmethod
# Create a Person class with:
#   - __init__(self, name, age)
#   - @classmethod from_string(cls, s) → takes "Alice-30", splits it, returns a Person object
#   - @staticmethod is_adult(age) → returns True if age >= 18
#
# Difference:
#   classmethod  → gets the class (cls) as first arg, used as alternative constructor
#   staticmethod → no self or cls, just a utility function that lives in the class namespace
#
# Test:
#   p = Person.from_string("Alice-30")
#   print(Person.is_adult(16))  → False
