def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?"""
    
    if isinstance(collection, (list, str, tuple)):
        # For lists, strings, and tuples
        if start is not None:
            sub_collection = collection[start:]
        else:
            sub_collection = collection

        return sought in sub_collection

    elif isinstance(collection, set):
        # For sets, "start" is ignored
        return sought in collection

    elif isinstance(collection, dict):
        # For dictionaries, check if sought is a value in the dictionary
        return sought in collection.values()

    return False

# Test cases
print(includes([1, 2, 3], 1))                  # Output: True
print(includes([1, 2, 3], 1, 2))               # Output: False
print(includes("hello", "o"))                  # Output: True
print(includes(('Elmo', 5, 'red'), 'red', 1))  # Output: True
print(includes({1, 2, 3}, 1))                 # Output: True
print(includes({1, 2, 3}, 1, 3))              # Output: True (start is ignored for sets)
print(includes({"apple": "red", "berry": "blue"}, "blue"))  # Output: True
