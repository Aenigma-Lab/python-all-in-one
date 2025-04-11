# We can use enumerate function with for loop to track 
#position of our item in iterable 

# How we can do this without enumerate function

names = ['shubham','Rahul','kamlesh','aman','Mahesh']

for i in names:
    print(f"{names.index(i)}->->->{i}")


# another method is 
indx = 0
for i in names:
   print(f"{indx}>>>>>>>{i}")
   indx+=1

#Above example in using Enumerate function....

for position, name_list in enumerate(names):
    print(f"{position}==========>{name_list}")

# Using Enumerate funion to do this ......
count = [1,5,6,22,0,5,7]
for indx, number in enumerate(count):
    print(f"{indx}------->{number}")




# Solve a small problem 


#1) Define a function that take two arguments
#2) List contaning string
#3) String that want to find in your list
#4) and this function will return the index of string in your list and 
#5) If string is not present then return -1 
names = ['shubham','manish','ramesh','suresh','mahesh','vivek']
def find_position(names, target_name):
    for position, name in enumerate(names):
        if  name.lower() == target_name.lower():
            return position   
    return -1
        
finded_name  = find_position(names, "suresh")

print(finded_name)

