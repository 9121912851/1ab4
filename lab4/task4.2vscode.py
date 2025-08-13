# Few-shot prompts for writing a function that counts the number of vowels in a string.
# The function will take input from provided examples automatically.

examples = [
    "hello world",
    "Python Programming",
    "AI Assistant",
    "vowels",
    "sky"
]

def count_vowels(s):
    vowels = set("aeiouAEIOU")
    return sum(1 for char in s if char in vowels)

for example in examples:
    print(f"Input: '{example}' -> Number of vowels: {count_vowels(example)}")