def titleize(phrase):
    """Return phrase in title case (each word capitalized)."""
    # Split the phrase into words using whitespace as the separator
    words = phrase.split()
    
    # Capitalize each word in the list and join them with a space
    titleized_phrase = ' '.join(word.capitalize() for word in words)

    return titleized_phrase

# Test cases
print(titleize('this is awesome'))          # Output: 'This Is Awesome'
print(titleize('oNLy cAPITALIZe fIRSt'))    # Output: 'Only Capitalize First'
