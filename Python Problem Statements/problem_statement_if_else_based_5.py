#EXERCISE - WATCH COCO (its a movie name)
# condition is that:

# Ask user's name and age

# If user's name start with ('a' or "A") and age is above 10 then

# Print 'You can watch coco movie.'

# Else print 'Sorry , you can not watch coco.'

user_name  = input("Enter you name : ").strip().lower()
age = int(input("Enter your age : "))
print(f"{user_name}and age is {age}")

if user_name[0] == 'a' and age >= 10:
  print("You can watch coco movie.")
else:
  print("Sorry, you can not watch coco.")


#we can also use this conditon then dont use lower() method
#if age >= 10 and (user_name[0] == 'a' or user_name == 'A')