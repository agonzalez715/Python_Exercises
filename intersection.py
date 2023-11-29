def intersection(l1, l2):
    """Return intersection of two lists as a new list."""
    # Use a list comprehension to create a new list containing elements that are common in both l1 and l2
    return [item for item in l1 if item in l2]

# Test cases
print(intersection([1, 2, 3], [2, 3, 4]))        # Output: [2, 3]
print(intersection([1, 2, 3], [1, 2, 3, 4]))    # Output: [1, 2, 3]
print(intersection([1, 2, 3], [3, 4]))          # Output: [3]
print(intersection([1, 2, 3], [4, 5, 6]))        # Output: []
