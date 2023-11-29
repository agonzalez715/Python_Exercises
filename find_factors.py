def find_factors(num):
    """Find factors of num, in increasing order."""
    factors = []

    # Iterate from 1 to num (inclusive)
    for i in range(1, num + 1):
        # Check if i is a factor of num
        if num % i == 0:
            factors.append(i)

    return factors

# Test cases
print(find_factors(10))      # Output: [1, 2, 5, 10]
print(find_factors(11))      # Output: [1, 11]
print(find_factors(111))     # Output: [1, 3, 37, 111]
print(find_factors(321421))  # Output: [1, 293, 1097, 321421]

