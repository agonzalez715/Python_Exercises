def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive."""
    # Initialize an empty dictionary to store vowel counts
    vowel_counts = {}
    
    # Define the set of vowels in both uppercase and lowercase
    vowels = set("AEIOUaeiou")
    
    # Iterate through each character in the phrase
    for char in phrase:
        # Check if the character is a vowel
        if char in vowels:
            # Convert the character to lowercase for case-insensitivity
            char = char.lower()
            # Increment the count for the vowel in the dictionary
            vowel_counts[char] = vowel_counts.get(char, 0) + 1

    return vowel_counts

# Test cases
print(vowel_count('rithm school'))  # Output: {'i': 1, 'o': 2}
print(vowel_count('HOW ARE YOU? i am great!'))  # Output: {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
