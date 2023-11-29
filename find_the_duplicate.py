def find_the_duplicate(nums):
    """Find the duplicate number in nums."""
    # Create an empty set to store encountered numbers
    seen = set()
    
    # Iterate through the list of numbers
    for num in nums:
        # If the number is already in the set, it's a duplicate
        if num in seen:
            return num
        # Otherwise, add it to the set
        seen.add(num)
    
    # If no duplicate is found, return None
    return None

# Test cases
print(find_the_duplicate([1, 2, 1, 4, 3, 12]))     # Output: 1
print(find_the_duplicate([6, 1, 9, 5, 3, 4, 9]))  # Output: 9
print(find_the_duplicate([2, 1, 3, 4]))           # Output: None
