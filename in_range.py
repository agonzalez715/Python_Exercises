def in_range(nums, lowest, highest):
    """Print numbers inside range."""
    
    # Loop through each number in the nums list
    for num in nums:
        # Check if the current number is within the specified range
        if lowest <= num <= highest:
            print(f"{num} fits")

# Test the function with in_range([10, 20, 30, 40, 50], 15, 30)
in_range([10, 20, 30, 40, 50], 15, 30)
