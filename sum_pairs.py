def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal."""
    seen_numbers = set()
    
    for num in nums:
        complement = goal - num
        if complement in seen_numbers:
            return (complement, num)
        seen_numbers.add(num)
    
    return ()

# Test cases
print(sum_pairs([1, 2, 2, 10], 4))              # Output: (2, 2)
print(sum_pairs([4, 2, 10, 5, 1], 6))           # Output: (4, 2)
print(sum_pairs([5, 1, 4, 8, 3, 2], 7))         # Output: (4, 3)
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))     # Output: ()
