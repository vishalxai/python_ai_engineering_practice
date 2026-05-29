# Q39 — Power Features: Type Hints
# Add full type hints to all of these functions.
# Do NOT change the logic — only add annotations.
#
# from typing import Optional

def greet(name):
    return f"Hello, {name}"

def get_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

def find_user(users, user_id):
    # Returns the user dict if found, None if not
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def merge_configs(default, override):
    # Merges two dicts, override takes priority
    return {**default, **override}
