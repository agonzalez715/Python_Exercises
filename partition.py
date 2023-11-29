def partition(lst, fn):
    """Partition lst by predicate."""
    # Initialize two empty lists for the items that pass and fail the predicate
    passed_items = []
    failed_items = []

    # Iterate through each item in the list
    for item in lst:
        # Apply the predicate function and check if it returns True
        if fn(item):
            passed_items.append(item)
        else:
            failed_items.append(item)

    # Return a list containing both the passed and failed items
    return [passed_items, failed_items]

# Test cases
def is_even(num):
    return num % 2 == 0

def is_string(el):
    return isinstance(el, str)

print(partition([1, 2, 3, 4], is_even))          # Output: [[2, 4], [1, 3]]
print(partition(["hi", None, 6, "bye"], is_string))  # Output: [['hi', 'bye'], [None, 6]]
