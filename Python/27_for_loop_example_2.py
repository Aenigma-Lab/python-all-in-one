# practice for loop 
# ask user name and count each character
# 'Shubham Mishra'
# s : 1
# h : 2
# u : 1
# b : 1
# a : 1
# m : 1

user_name = input("enter you name to count Characters: ")
temp = ""
for i in range(len(user_name)):
  if user_name[i] not in temp:
    temp += (user_name[i])
    print(f"{user_name[i]}  :  {user_name.count(user_name[i])}")
   
