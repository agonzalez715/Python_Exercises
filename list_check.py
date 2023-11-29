def list_check(lst):
    """Are all items in lst a list?"""
    # Use a list comprehension to check if each item is a list
    return all(isinstance(item, list) for item in lst)

# Test cases
print(list_check([[1], [2, 3]]))  # Output: True
print(list_check([[1], "nope"]))   # Output: False
