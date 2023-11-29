def two_oldest_ages(ages):
    """Return two distinct oldest ages as a tuple (second-oldest, oldest)."""
    # Remove duplicates and sort the list of ages in descending order
    unique_ages = sorted(set(ages), reverse=True)
    
    # Get the two oldest ages
    if len(unique_ages) >= 2:
        return (unique_ages[1], unique_ages[0])
    else:
        return (unique_ages[0], unique_ages[0])  # If there's only one age, return it twice

# Test cases
print(two_oldest_ages([1, 2, 10, 8]))      # Output: (8, 10)
print(two_oldest_ages([6, 1, 9, 10, 4]))  # Output: (9, 10)
print(two_oldest_ages([1, 5, 5, 2]))      # Output: (2, 5)

