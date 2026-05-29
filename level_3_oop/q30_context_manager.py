# Q30 — OOP: Context Manager (__enter__ and __exit__)
# Create a class ManagedFile that works as a context manager:
#   - __init__(self, filename, mode)
#   - __enter__ → opens the file and returns the file object
#   - __exit__  → closes the file (even if an exception occurred)
#
# Usage should look like:
#   with ManagedFile("test.txt", "w") as f:
#       f.write("hello")
#
# This is how Python's built-in open() works internally.
# After writing, also implement the same thing using @contextmanager from contextlib.
