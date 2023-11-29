def sum_nums(nums):
    """Given list of numbers, return sum of those numbers."""
    
    # Initialize a variable to store the sum
    total = 0
    
    # Loop through each number in the list
    for num in nums:
        # Add the current number to the total
        total += num
    
    return total

# Test the function with sum_nums([1, 2, 3, 4])
result = sum_nums([1, 2, 3, 4])
print("sum_nums returned", result)
