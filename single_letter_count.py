def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?"""
    # Convert both the word and letter to lowercase to make the comparison case-insensitive
    word = word.lower()
    letter = letter.lower()

    # Use the count method to count the occurrences of the letter in the lowercase word
    return word.count(letter)

# Test cases
print(single_letter_count('Hello World', 'h'))  # Output: 1
print(single_letter_count('Hello World', 'z'))  # Output: 0
print(single_letter_count("Hello World", 'l'))  # Output: 3
