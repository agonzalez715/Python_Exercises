def sum_up_diagonals(matrix):
    """Return the sum of diagonals in a square matrix."""
    # Initialize variables to store the sums of the two diagonals
    diagonal1_sum = 0
    diagonal2_sum = 0
    
    # Get the number of rows in the matrix
    num_rows = len(matrix)
    
    # Iterate through the rows of the matrix
    for i in range(num_rows):
        # Add the element at the i-th row and i-th column to diagonal1_sum
        diagonal1_sum += matrix[i][i]
        
        # Add the element at the i-th row and (num_rows - i - 1)-th column to diagonal2_sum
        diagonal2_sum += matrix[i][num_rows - i - 1]
    
    # Return the sum of both diagonals
    return diagonal1_sum + diagonal2_sum

# Test cases
m1 = [
    [1,   2],
    [30, 40],
]
print(sum_up_diagonals(m1))  # Output: 73

m2 = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9],
]
print(sum_up_diagonals(m2))  # Output: 30
