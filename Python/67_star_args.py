def all_total(*args):
    """Calculate the sum of all provided arguments."""
    
    # Print the arguments received
    print("Arguments received:", args)
    
    # Print the type of 'args' to show it is a tuple
    print("Type of arguments:", type(args))  # args is a tuple
    
    # Initialize total to zero
    total = 0
    
    # Iterate through each number in args
    for number in args:
        total += number  # Add each number to the total
    
    return total  # Return the final total

# Example 1: Basic Usage
result1 = all_total(1, 2, 3, 4, 5)  
print("Total of Example 1:", result1)  # Output: 15

# Example 2: More Numbers
result2 = all_total(10, 20, 30, 40, 50)
print("Total of Example 2:", result2)  # Output: 150

# Example 3: Single Number
result3 = all_total(7)
print("Total of Example 3:", result3)  # Output: 7

# Example 4: No Numbers
result4 = all_total()  
print("Total of Example 4:", result4)  # Output: 0

# Example 5: Mixed Data Types (floats)
result5 = all_total(1.5, 2.5, 3.5)
print("Total of Example 5:", result5)  # Output: 7.5

# Example 6: Negative Numbers
result6 = all_total(-1, -2, -3, -4)
print("Total of Example 6:", result6)  # Output: -10

# Example 7: Large Number of Arguments
result7 = all_total(*range(1, 101))  # Using unpacking to sum numbers from 1 to 100
print("Total of Example 7:", result7)  # Output: 5050
