def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# Example input-output for a function that counts the number of vowels in a string:
# Input: hello
# Output: 2

# Input: AIAC
# Output: 2

# Take auto input from examples
examples = ["hello", "AIAC", "Python", "vowel", "sky"]

for example in examples:
    print(f"Input: {example}")
    print(f"Output: {count_vowels(example)}\n")
