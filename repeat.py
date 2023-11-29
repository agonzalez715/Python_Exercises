def repeat(phrase, num):
    """Return phrase, repeated num times."""
    if not isinstance(num, int) or num < 0:
        return None

    return phrase * num

# Test cases
print(repeat('*', 3))     # Output: '***'
print(repeat('abc', 2))   # Output: 'abcabc'
print(repeat('abc', 0))   # Output: ''
print(repeat('abc', -1) is None)  # Output: True (num is not a positive integer)
print(repeat('abc', 'nope') is None)  # Output: True (num is not an integer)
