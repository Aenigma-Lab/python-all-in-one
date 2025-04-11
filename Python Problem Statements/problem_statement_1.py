# ask user to input 3 numbers and you have to print average of theree numbers using string formattting.
# try to take all three comma seprated inputs in one line.

num_one, num_two, num_three = (input("enter three number with comma seperated. ")).split(",")

sum = int(num_one)+int(num_two)+int(num_three)

average = sum/3

print(f" the average of thee number is {average} ")
