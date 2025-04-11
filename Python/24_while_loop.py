# loops
# while loop
# SYNTAX ====> **while CONDITION: STATEMENT**
#############imp####################
i = 3
while i <= 10: print(i); i += 1
#################imp######################
# WHILE LOOP SYNTAX

# INITIALIZE A VARIABLE
# This is the variable that will be tested in the loop condition.
# Example: i = 1

i = 1

# WHILE LOOP CONDITION
# This is the condition that is checked before each iteration.
# The loop will continue to run as long as this condition evaluates to True.
# Example: while i <= 10:

while i <= 10:
    
    # BODY OF THE LOOP
    # This is the code that runs during each iteration of the loop.
    # Example: print(i)
    print(i)
    
    # UPDATE THE VARIABLE
    # This statement updates the variable that is part of the loop condition.
    # If not updated correctly, it may cause an infinite loop.
    # Example: i += 1
    
    i += 1

# AFTER THE LOOP
# This code runs after the loop has terminated (i.e., when the condition is False).
# Example: print("Loop has ended.")

##################################################3

i = 1
while i<=10:
  print(f"hello shubham {i}")
  i+=1
  
print("""...........
...........
...........""")


###################################################


# while loop when you want to scip the particular sequence form the loop. 
###################################################
i = 2
while i <= 10:
    if i == 5:
        i += 1  # Increment i to avoid infinite loop
        continue  # Skip the rest of the loop body for i == 3
    print(i)
    i += 1

##################################################