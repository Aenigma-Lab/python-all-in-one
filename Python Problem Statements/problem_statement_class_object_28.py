# Question:: suppose you  have laptop  shop and and you want to give discount on lapoop by default is 10 percent on price
# but some laptop you want to give diffrent discount then write code to implement this using class object and instace function using very reliable method.



class Laptop:
    discount_percent = 10
    def __init__(self, brand, model, price):
        self.laptop_brand = brand
        self.laptop_model = model
        self.laptop_price = price

    def laptop_discount(self):
        discount_price = (self.discount_percent/100)*self.laptop_price # use self.discount_percent
        return self.laptop_price - discount_price
    

laptop_1 = Laptop('Dell','DL890',9000)
laptop_2 = Laptop('Vivo','Vi9802',10000)
# suppose i want to give diffent discount on diffrent laptop 
laptop_3 = Laptop('Lenovo','Len983',100000)
laptop_3.discount_percent = 30
print(laptop_3.laptop_discount())

print(laptop_1.laptop_discount())
print(laptop_2.laptop_discount())


print(laptop_3.__dict__)

