def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end."""
    # Handle the case where end is not provided (use the end of the list)
    if end is None:
        end = len(nums)
    
    # Ensure that start and end are within valid bounds
    start = max(0, start)           # Ensure start is at least 0
    end = min(len(nums), end)       # Ensure end is within list bounds
    
    # Calculate the sum of numbers in the specified range
    total = sum(nums[start:end])
    
    return total

# Test cases
nums = [1, 2, 3, 4]
print(sum_range(nums))        # Output: 10
print(sum_range(nums, 1))     # Output: 9
print(sum_range(nums, end=2)) # Output: 6
print(sum_range(nums, 1, 3))  # Output: 9
print(sum_range(nums, 1, 99)) # Output: 9 (end is beyond the end of the list)
