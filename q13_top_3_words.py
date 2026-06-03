# Q13 — Level 3: Functions and Real Patterns
# Write a function: top_3_words(text)
# It takes a string and returns the 3 most frequently occurring words.
#
# Example:
# text = "the cat sat on the mat the cat"
# top_3_words(text) → ["the", "cat", "sat"]  (or similar top-3 by count)

def top_3_words(text):
    freq = {}
    words = text.split()
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1 

    return sorted(freq,key=lambda w:freq[w],reverse=True)[:3]
print(top_3_words("the cat sat on the mat the cat"))


    
