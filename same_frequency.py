def same_frequency(num1, num2):
    """Do these nums have the same frequencies of digits?"""
    # Convert the numbers to strings
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Initialize dictionaries to store digit frequencies
    freq1 = {}
    freq2 = {}
    
    # Count the occurrences of each digit in num1
    for digit in str_num1:
        freq1[digit] = freq1.get(digit, 0) + 1
    
    # Count the occurrences of each digit in num2
    for digit in str_num2:
        freq2[digit] = freq2.get(digit, 0) + 1
    
    # Compare the dictionaries to check if they have the same frequencies
    return freq1 == freq2

# Test cases
print(same_frequency(551122, 221515))   # Output: True
print(same_frequency(321142, 3212215))  # Output: False
print(same_frequency(1212, 2211))      # Output: True
