#dictionary comprehension
# square = {1:1, 2:4, 3:9}

square  = {num:num**2 for num in range(1,11)}
print(square)


# we can also use fstring to print 

f_square  = {f"Squrare of {num} is ":num**2 for num in range(1,11)}
print(f_square)

#we can use for loop to print next line.
square_for_loop  = {num:num**2 for num in range(1,11)}

for i, j in square_for_loop.items():
    print(f"{i} : {j}")


# How many time character in string count it.
string = 'shubhammishra'
word_count = {char:string.count(char) for char in string}
print(word_count)