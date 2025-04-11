# if elif else statment

# show ticket pricing
# 1 to 3 (free)
# 4 to 10 (150 rupees)
# 11 to 60 (250 rupees)
# above 60 (200 rupees)


age = int(input("Enter your age : "))

if age > 0 and age <= 3: #or can write [0<age<=3]
  print("you can watch free show")

elif age > 3 and age <= 10: #or can write [3<age<=10]
  print("show price 150 rupees.")

elif age > 10 and age <= 60:#or can write [10<age<=60]
  print("show price 250 rupees.")

elif age > 60:
  print("show price is 200") 

else: 
  print("oops!! wrong age")