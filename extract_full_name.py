def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts."""
    # Use a list comprehension to extract and combine first and last names
    return [f"{person['first']} {person['last']}" for person in people]

# Test case
names = [
    {'first': 'Ada', 'last': 'Lovelace'},
    {'first': 'Grace', 'last': 'Hopper'},
]

print(extract_full_names(names))  # Output: ['Ada Lovelace', 'Grace Hopper']
