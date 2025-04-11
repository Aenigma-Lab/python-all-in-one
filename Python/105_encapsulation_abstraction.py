# In this series we will talk about 
# Encapsulation
# Abstraction
# Some special naming convention
# Naming Mangling
# python uses tim short method. s

# __name() # this is not a convention

class Phone:
    def __init__(self, brand, model_name, price):
        self.__brand = brand
        self.model_name = model_name
        self._price = price # according to naming convention (_price) it consider as private but noting is private in python

    def make_a_call(self, phone_number):
        print(f"calling {phone_number}....")

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
# _name # convention of private name 
# __name__ # it is called (dunder) or magic method.



phone_1 = Phone('nokia','1100',1000)
print(phone_1._price)
phone_1._price = -1000 #if i change the price of phone
print(phone_1._price)

print(phone_1.__dict__) #{'brand': 'nokia', '_Phone__model_name': '1100', '_price': -1000}

#------>>>>>   '_Phone__model_name' # this is not private 
phone_1._Phone__brand = 'samsung'
print(phone_1._Phone__brand)
