# string indexing?
# so suppose we have a string language = "python" so in python it is called indexing if i want to print a single character then also i can print in the .
# String indexing (indexing start with 0)
language = "python"

#position here 
# string      starting_position  startwith_ending_position
# p     =     0                  -6
# y     =     1                  -5
# t     =     2                  -4
# h     =     3                  -3
# o     =     4                  -2
# n     =     5                  -1

# if I want to print any particuler characher from the string then put the indx number we can do like this.
#STARTING POSITION
print(language[1])

print(language[4])

#print(language[6])                                                  #"IndexError: string index out of range". because here only index number till 5 only and its searching index 6 and index 6 is not present so it is not accessible, thats why it throwing out of range error.

#ENDING POSITION 
print(language[-1])
print(language[-6])