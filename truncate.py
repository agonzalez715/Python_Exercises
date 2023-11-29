def truncate(phrase, n):
    """Return truncated-at-n-chars version of phrase."""
    
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    
    if len(phrase) <= n:
        return phrase
    
    return phrase[:n - 3] + '...'

# Test cases
print(truncate("Hello World", 6))  # Output: 'Hel...'
print(truncate("Problem solving is the best!", 10))  # Output: 'Problem...'
print(truncate("Yo", 100))  # Output: 'Yo'
print(truncate('Cool', 1))  # Output: 'Truncation must be at least 3 characters.'
print(truncate("Woah", 4))  # Output: 'W...'
print(truncate("Woah", 3))  # Output: '...'
