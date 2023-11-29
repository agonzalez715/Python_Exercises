def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d."""
    # Get the keys from the dictionary as a list
    keys = list(d.keys())
    
    # Find the minimum and maximum keys using the min() and max() functions
    min_key = min(keys)
    max_key = max(keys)
    
    # Return the minimum and maximum keys as a tuple
    return (min_key, max_key)

# Test cases
print(min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}))  # Output: (1, 10)

print(min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"}))  # Output: ('apple', 'cherry')
