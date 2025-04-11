#raise errors example 1
#NotImplementedError
#abstract method----there is not abstract method in pyhon it is only in java.

class Animal():
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError('you have to defice this method in subclass.')
        # return "This is animal sound."
    
class Dog(Animal):
    def __init__(self,name,bread):
        super().__init__(name)
        self.bread = bread

    def sound(self):
        return "Bhau Bhau Bhau"


class Cat(Animal):
    def __init__(self,name,bread):
        super().__init__(name)
        self.bread = bread

    def sound(self):
        return "Meau Meau Mau"


cat = Cat('oto','koto')
print(cat.sound())

# animal = Animal('kutu')
# print(animal.sound())

dog = Dog('suttu','pub')
print(dog.sound())