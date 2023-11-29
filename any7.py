def any7(nums):
     """Are any of these numbers a 7? (True/False)"""
    
    # Loop through each number in the list
    for num in nums:
        # Check if the current number is equal to 7
        if num == 7:
            return True  # If we find a 7, return True
    
    # If we didn't find any 7 in the list, return False
    return False 

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

