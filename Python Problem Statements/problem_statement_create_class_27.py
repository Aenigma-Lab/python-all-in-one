# Question:  Create a laptop class with attributes like brand name, model name, price
# Create two objects/instance of your laptop class



class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.laptop_brand_name = brand_name
        self.laptop_model_name = model_name
        self.laptop_price = price
        self.laptop_name = brand_name +' '+model_name

laptop_1 = Laptop('Dell','DL001',2699999)
laptop_2 = Laptop('Asus','AS0001',309999)


print(laptop_1.laptop_name)

print(laptop_1.laptop_brand_name)
print(laptop_1.laptop_model_name)
print(laptop_2.laptop_brand_name)