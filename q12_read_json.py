# Q12 — Level 3: Functions and Real Patterns
# Write a function: load_json(filepath)
# It reads a JSON file from the given path and returns its contents as a Python dict.
# Handle the case where the file does not exist — return None in that case.
#
# You can test it by creating a small sample.json file with any content.


import json

def load_json(filepath):
    try:
        with open(filepath,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None
    
data = load_json('sample.json')
if data:
    print(json.dumps(data,indent=4))
else:
    print("File not found or invalid JSON.")

print(load_json('missing.json'))
