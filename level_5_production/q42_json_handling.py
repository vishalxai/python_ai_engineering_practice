# Q42 — Production: JSON Handling
# Write these functions:
#
# 1. save_json(data, filepath) → saves a dict to a JSON file (pretty-printed, indent=2)
# 2. load_json(filepath) → loads and returns JSON as a dict, returns None if file not found
# 3. get_nested(data, *keys) → safely get a nested value, return None if any key is missing
#    Example: get_nested(data, "user", "address", "city") instead of data["user"]["address"]["city"]
#
# import json
