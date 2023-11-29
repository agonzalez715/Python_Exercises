def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end."""
    if command == 'remove':
        if location == 'beginning':
            return lst.pop(0) if lst else None
        elif location == 'end':
            return lst.pop() if lst else None
    elif command == 'add':
        if location == 'beginning':
            lst.insert(0, value)
            return lst
        elif location == 'end':
            lst.append(value)
            return lst
    return None

# Test cases
lst = [1, 2, 3]

# Remove from end
print(list_manipulation(lst, 'remove', 'end'))  # Output: 3

# Remove from beginning
print(list_manipulation(lst, 'remove', 'beginning'))  # Output: 1

# Verify the updated list after removal
print(lst)  # Output: [2]

# Add to beginning
print(list_manipulation(lst, 'add', 'beginning', 20))  # Output: [20, 2]

# Add to end
print(list_manipulation(lst, 'add', 'end', 30))  # Output: [20, 2, 30]

# Verify the updated list after addition
print(lst)  # Output: [20, 2, 30]

# Invalid commands or locations
print(list_manipulation(lst, 'foo', 'end') is None)  # Output: True
print(list_manipulation(lst, 'add', 'dunno') is None)  # Output: True
