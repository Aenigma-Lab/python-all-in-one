# we can use getter() decoartor as ---> @property 
# and can use setter() decorator as ----> setter

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = max(price,0)
        # insted of this we can write above trick for handle negative price.
        # if price > 0: 
        #     self.price = price
        # else:
        #     self.price = 0
    
        # self.full_specification = f"company name is {self.brand} and modle is {self.model} and price is {self.price}"

    # here if i use @property  then we dont need to call as function
    @property
    def full_specification(self):
        print(f"company name is {self.brand} and modle is {self.model} and price is {self.price}")

    #getter() and setter()----> not any one can set price negative we must make setter decorator after @property decorator.
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        self._price = max(new_price,0)



    def calling(self, phone_number):
        print(f"calling from {phone_number}.")

    
    def some_mobile_detail(self):
        print(f"mobile brand is {self.brand} and its modle number is {self.model}")
# it should not take negative price
phone_1 = Phone('Samsung','sm40',19999)
print(phone_1.full_specification)
# i want to change the price of samsung device price chnaged but phone_1 full specificaiton price is still not chnaged.
phone_1.price = -20000
print(phone_1.price)


#this will call as function......
# print(phone_1.full_specification())## will get update price using this type method.

# i use @property decorator so not need to call as function it will call like property or like attribute

print(phone_1.full_specification) #--it will call like attribute
