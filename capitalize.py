def capitalize(phrase):
    """Capitalize first letter of first word of phrase."""
    # Check if the phrase is not empty
    if phrase:
        # Capitalize the first letter of the first word
        return phrase[0].upper() + phrase[1:]
    else:
        # Return an empty string if the phrase is empty
        return ""

# Test cases
print(capitalize('python'))           # Output: 'Python'
print(capitalize('only first word'))  # Output: 'Only first word'
