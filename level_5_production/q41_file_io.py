# Q41 — Production: File I/O
# Write three functions:
#
# 1. write_file(filepath, content) → writes content to a file (overwrites if exists)
# 2. read_file(filepath) → reads and returns the content, returns None if file not found
# 3. append_file(filepath, line) → appends a line to the file
#
# Use the `with open(...)` pattern — never open files without a context manager.
# Handle FileNotFoundError in read_file.
#
# Test by writing, appending, then reading the file back.
