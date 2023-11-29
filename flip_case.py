def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase."""
    # Initialize an empty result string
    result = ""

    # Iterate through each character in the phrase
    for char in phrase:
        # Check if the character matches the character to swap (ignoring case)
        if char.lower() == to_swap.lower():
            # Flip the case and add it to the result
            result += char.swapcase()
        else:
            # Keep the character as-is and add it to the result
            result += char

    return result

# Test cases
print(flip_case('Aaaahhh', 'a'))  # Output: 'aAAAhhh'
print(flip_case('Aaaahhh', 'A'))  # Output: 'aAAAhhh'
print(flip_case('Aaaahhh', 'h'))  # Output: 'AaaaHHH'
