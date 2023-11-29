def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?"""
    # Extract the list of hobbies for each friend
    hobbies_a = set(a[2])
    hobbies_b = set(b[2])

    # Check if there is an intersection of hobbies between the two friends
    return bool(hobbies_a.intersection(hobbies_b))

# Test cases
elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

print(friend_date(elmo, sauron))  # Output: False
print(friend_date(sauron, gandalf))  # Output: True
