def find_greater_numbers(nums):
    """Return the number of times a number is followed by a greater number."""
    count = 0  # Initialize a count variable to keep track of the occurrences
    
    # Iterate through the list using a nested loop
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):  # Start from the next index
            if nums[i] < nums[j]:
                count += 1
    
    return count

# Test cases
print(find_greater_numbers([1, 2, 3]))      # Output: 3
print(find_greater_numbers([6, 1, 2, 7]))  # Output: 4
print(find_greater_numbers([5, 4, 3, 2, 1]))  # Output: 0
print(find_greater_numbers([]))             # Output: 0
