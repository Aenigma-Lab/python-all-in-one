# instead using selft we can use any thing 
# we have to use only 'self' according to convetion

#example #-----------------------here 'self' is not using.
class Animal:
    def __init__(animal,type, sound):
        animal.type = type
        animal.sound = sound

dog = Animal('dog','barking')
cat = Animal('cat','meaou')

print(dog.type)
print(cat.type)


# 2nd example---------------Here 'self' is using.

class Person:
    def __init__(self, first_name, last_name, age):
        print("init method / constructor get called.")
        #instance varialbes
        self.person_first_name = first_name
        self.person_last_name = last_name
        self.age = age


person_1 = Person('shubham','mishra',25) #this is object
person_2 = Person('Nikhil','gupta',24)# this is 2nd object

print(person_1.person_first_name)# this is calling variable object.variable
print(person_2.person_last_name)

print(person_2.age) # this is calling variable object.variable