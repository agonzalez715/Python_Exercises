def mode(nums):
    """Return most-common number in list."""
    # Create a dictionary to store the count of each number
    num_count = {}

    # Initialize variables to keep track of the most common number and its count
    most_common_num = None
    most_common_count = 0

    # Iterate through the list and count the occurrences of each number
    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

        # Update the most common number and its count if needed
        if num_count[num] > most_common_count:
            most_common_num = num
            most_common_count = num_count[num]

    return most_common_num

# Test cases
print(mode([1, 2, 1]))         # Output: 1
print(mode([2, 2, 3, 3, 2]))   # Output: 2

