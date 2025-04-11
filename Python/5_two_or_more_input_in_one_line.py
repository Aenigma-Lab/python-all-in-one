# by using split() method we can take more than two input in one line.in the split by default it will take space while inputing the data but we can also pass like split(",") comma Also. or can pass anything like split(":") like this.
name, age = input("enter your name and age ").split()
print(name, age)