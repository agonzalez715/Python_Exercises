def multiply_even_numbers(nums):
    """Multiply the even numbers."""
    # Initialize the result to 1
    result = 1

    # Iterate through each number in the list
    for num in nums:
        # Check if the number is even
        if num % 2 == 0:
            # Multiply the result by the even number
            result *= num

    return result

# Test cases
print(multiply_even_numbers([2, 3, 4, 5, 6]))  # Output: 48
print(multiply_even_numbers([3, 4, 5]))        # Output: 4
print(multiply_even_numbers([1, 3, 5]))        # Output: 1
