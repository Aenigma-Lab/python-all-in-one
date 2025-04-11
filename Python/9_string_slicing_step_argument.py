# string slicing
# step argument
# it means that how many "step" you want to take to print you sub strings.

# SYNTAX ==>[START ARGUMENT : STOP ARGUMENT-1 : STEP]

print("shubham"[0:5]) # this will by default take 1 setp

print("shubham"[0:6:2]) # this will take 2 step after each character.

#if not given any stop argument then it will go till end of the sting and if we not pass any start argument then will start witnn 0 index.

print(f"it will go with one by one character " +"shubham"[0:7:1])

print(f"it will go with two step character till end. here not pass the end argument of string." +"shubham"[0::2])

print(f"it will go with two step character till end. here not pass the start argument of string." +"shubham"[:5:3])


print(f"it will go with two step character till end. here not pass neither start nor end argument of string." +"shubham"[::2])

#reverse string 
name = "Shubham"
print(name[-1::-1]) # this will reverse the string
print(name[::-1]) # this will also reverse the string

#  !!!IMP!!! while we working with negative steop start string should be greater then the end string otherwise no output will come

print("Shubham"[4:6:-1]) #detial expain how it will work steip by step
# Let's break down the Python code print("Shubham"[5::-1]) step by step:

# String Details
# String: "Shubham"
# Indices: S → 0, h → 1, u → 2, b → 3, h → 4, a → 5, m → 6
# Slicing Breakdown
# In Python slicing, the syntax is string[start:stop:step]. Here's what each parameter means:

# start: The index where the slice begins.
# stop: The index where the slice ends (but does not include this index).
# step: The step size or direction of slicing (positive for forward, negative for backward).
# In the code "Shubham"[5::-1]:

# 5 is the start index.
# stop is omitted, so it defaults to the beginning of the string.
# step is -1, which means slicing in reverse order.
# Detailed Explanation
# Start Index: The slice begins at index 5, which corresponds to the character 'a'.

# Step: With a step of -1, the slicing direction is reversed. This means the slicing will proceed backwards from the start index.

# Stop Index: Since stop is omitted and step is negative, the slice will continue until it reaches the beginning of the string.

# Execution
# Let's see how the slicing would work step-by-step:

# Start at Index 5: 'a' (index 5)
# Move Backwards:
# Index 4 → 'h'
# Index 3 → 'b'
# Index 2 → 'u'
# Index 1 → 'h'
# Index 0 → 'S'
# So, when you slice from index 5 backwards to the beginning of the string, you collect characters in the reverse order from 'a' to 'S'.

# Output
# The resulting substring is 'ahbuhS'.





print("Shubham"[5::-1]) 
# detail explanation 
# Let's break down the Python code print("Shubham"[5::-1]) step by step:

# String Details
# String: "Shubham"
# Indices: S → 0, h → 1, u → 2, b → 3, h → 4, a → 5, m → 6
# Slicing Breakdown
# In Python slicing, the syntax is string[start:stop:step]. Here's what each parameter means:

# start: The index where the slice begins.
# stop: The index where the slice ends (but does not include this index).
# step: The step size or direction of slicing (positive for forward, negative for backward).
# In the code "Shubham"[5::-1]:

# 5 is the start index.
# stop is omitted, so it defaults to the beginning of the string.
# step is -1, which means slicing in reverse order.
# Detailed Explanation
# Start Index: The slice begins at index 5, which corresponds to the character 'a'.

# Step: With a step of -1, the slicing direction is reversed. This means the slicing will proceed backwards from the start index.

# Stop Index: Since stop is omitted and step is negative, the slice will continue until it reaches the beginning of the string.

# Execution
# Let's see how the slicing would work step-by-step:

# Start at Index 5: 'a' (index 5)
# Move Backwards:
# Index 4 → 'h'
# Index 3 → 'b'
# Index 2 → 'u'
# Index 1 → 'h'
# Index 0 → 'S'
# So, when you slice from index 5 backwards to the beginning of the string, you collect characters in the reverse order from 'a' to 'S'.

# Output
# The resulting substring is 'ahbuhS'.

# Thus, print("Shubham"[5::-1]) will output:

# Copy code
# ahbuhS
# print("Shubham"[4:6:-1])
# ChatGPT
# Let's analyze the code print("Shubham"[4:6:-1]) step by step:

# String Details
# String: "Shubham"
# Indices: S → 0, h → 1, u → 2, b → 3, h → 4, a → 5, m → 6
# Slicing Breakdown
# In Python slicing, the syntax is string[start:stop:step]. Here’s what each parameter means:

# start: The index where the slice begins.
# stop: The index where the slice ends (but does not include this index).
# step: The step size or direction of slicing.
# In the code "Shubham"[4:6:-1]:

# 4 is the start index.
# 6 is the stop index.
# -1 is the step, which means slicing in reverse order.
# Detailed Explanation
# Start Index: The slice begins at index 4, which corresponds to the character 'h'.

# Step: With a step of -1, the slicing direction is reversed.

# Stop Index: The slice stops when it reaches the stop index (but does not include it). Since the stop index is 6, the slicing will end before this index.

# Execution
# When using a negative step, the start index must be greater than the stop index to produce a result. If the start index is less than or equal to the stop index, the result will be an empty string because the slicing direction doesn’t match the range specified.

# In this case:

# Start at Index 4: 'h' (index 4)
# Move Backwards:
# Index 3 → 'b'
# Index 2 → 'u'
# Index 1 → 'h'
# Index 0 → 'S'
# Stop Before Index 6: This part is tricky because we are moving backwards, but the stop index 6 is to the right of the start index 4. Hence, the slice will not capture any characters.
# Output
# Since the stop index 6 is greater than the start index 4 when using a negative step, no characters fall into this slice range, resulting in an empty string.

# Thus, print("Shubham"[4:6:-1]) will output:

# Copy code
# (an empty line)

# how its not falling the slicing range
# When working with Python slicing, the step parameter dictates the direction of the slicing, which must align with the start and stop parameters. Let's clarify why print"Shubham"[4:6:-1] 
print("Shubham"[4:6:-1])
# results in an empty string:

# Slicing Parameters
# start: Index where slicing begins.
# stop: Index where slicing ends (but does not include this index).
# step: Direction and interval of slicing. A positive step slices forward, while a negative step slices backward.
# Behavior with Negative Steps
# When using a negative step:

# The start index must be greater than the stop index.
# If start is less than or equal to stop, the slicing range is invalid for a negative step.
# Example Analysis: "Shubham"[4:6:-1]
# Start at Index 4: The character at index 4 is 'h'.
# Stop at Index 6: The character at index 6 is 'm'.
# With a step of -1, you’re asking Python to slice in reverse order. This means the slice starts at index 4 and tries to move backwards, but it needs to end before index 6.

# Why No Characters Are Included
# For a negative step (-1), Python will slice from start to stop but only if the start index is greater than the stop index.
# Since the start index (4) is not greater than the stop index (6), Python cannot perform this slicing operation in reverse, resulting in no characters being included.
# Illustrative Example
# Consider "Shubham"[4:2:-1] instead:

# Start at Index 4: 'h'
# Stop before Index 2: 'u'
# Step of -1: Slice backwards from index 4 to 3 to 2.
# This would produce 'hbu', showing that negative slicing requires the start to be greater than the stop.

# Summary
# For "Shubham"[4:6:-1]:

# Start (4): 'h'
# Stop (6): 'm'
# Step (-1): Requires the start to be greater than the stop.
# Since 4 is not greater than 6, slicing cannot be performed in reverse within this range, resulting in an empty string.

# Thus, the output is: empty