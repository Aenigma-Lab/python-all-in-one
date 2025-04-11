#  we ca n write if else statent else come after if . only else we can not write alone without if. But we can write if statemnt alone without if statement.

use_name, age = input("enter your name and age : ").strip().split()

if int(age) >= 18 : 
  print(f'your name is "{use_name}" and your age is {age}. you are eligible for voting.')
else:
  print("you can not vote for now.")