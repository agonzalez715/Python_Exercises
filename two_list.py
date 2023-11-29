def two_list_dictionary(keys, values):
    """Given keys and values, make a dictionary of those."""
    dictionary = {}

    # Iterate through the shorter of the two lists
    for i in range(min(len(keys), len(values))):
        dictionary[keys[i]] = values[i]

    # If there are more keys than values, set remaining keys to None
    if len(keys) > len(values):
        for key in keys[len(values):]:
            dictionary[key] = None

    return dictionary

# Test cases
print(two_list_dictionary(['x', 'y', 'z'], [9, 8, 7]))  # Output: {'x': 9, 'y': 8, 'z': 7}
print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': None}
print(two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4]))  # Output: {'a': 1, 'b': 2, 'c': 3}
