# here the height can not be greater than 2 meters.

height = int(input("Enter your height.: "))
weight = int(input("Enter your weight.: "))

if height > 2 or weight > 1000:
    raise ValueError("You input either wrong height or wrong weight.")
bmi = weight / height ** 2

print(bmi)