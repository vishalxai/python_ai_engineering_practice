# Q8 — Level 2: Collections
# Read a sentence from the user.
# Count how many times each word appears.
# Print the result as a dictionary.
# Example: "the cat sat on the mat" → {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}

user_sentence = list(input("Please input your sentence ").split())
freq = {}
for word in user_sentence:
    if word in freq:
        freq[word] += 1 
    else:
        freq[word] = 1 

print(freq)


