def last_element(lst):
    """Return last item in list (None if list is empty)."""
    if len(lst) > 0:
        return lst[-1]
    else:
        return None

# Test cases
print(last_element([1, 2, 3]))   # Output: 3
print(last_element([]) is None)  # Output: True
