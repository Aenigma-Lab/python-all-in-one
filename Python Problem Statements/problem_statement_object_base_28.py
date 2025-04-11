class Laptop:
    def __init__(self,model,name,price):
        self.laptop_model = model
        self.laptop_price = price
        self.laptop_name = name

    def laptop_discount(self, discount_percent):
       
        discount =  (discount_percent/100)*self.laptop_price
        return self.laptop_price - discount
    


laptop_1  = Laptop('AsusRog3050','Asus',100000)
print(laptop_1.laptop_discount(12))
