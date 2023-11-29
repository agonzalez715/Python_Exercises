def remove_every_other(lst):
    """Return a new list of other items."""
    # Use list slicing to create a new list with every other item
    return lst[::2]

# Test case
lst = [1, 2, 3, 4, 5]
result = remove_every_other(lst)

print(result)  # Output: [1, 3, 5]
print(lst)    # Output: [1, 2, 3, 4, 5] (original list is not mutated)
