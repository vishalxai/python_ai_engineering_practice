# Q45 — Production: HTTP Requests
# Write a function get_joke() that:
#   - Calls this free public API: https://official-joke-api.appspot.com/random_joke
#   - Returns a dict with {"setup": "...", "punchline": "..."}
#   - Handles: connection errors, non-200 status codes, JSON parse errors
#   - Uses a timeout of 5 seconds
#
# Write a second function get_multiple_jokes(n) that calls get_joke() n times
# and returns a list of jokes.
#
# import requests
