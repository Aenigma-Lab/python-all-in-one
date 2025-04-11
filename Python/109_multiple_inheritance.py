# Multiple Inheritace 

class A:
    def class_a_method(self):
        return 'I\'m just a class A method.'
    
    def hello(self):
        return 'hello form class A'
    

class B:
    def class_b_method(self):
        return 'I\'m just a class B method.'
    
    def hello(self):
        return 'hello form class B'
    

# class C(A,B):
#     pass


class C(B,A):
    pass

instance_c = C()
print(instance_c.class_a_method())
print(instance_c.class_b_method())
print(instance_c.hello()) # this will run from class B
# if i want to print B class hello() 
# check resolution order 

# if we want to print B() hello() method then change the order of C(B,A)

print(help(C))
    

# instance_a = A()
# print(instance_a.class_a_method())


print(C.mro())
# print(c.__mro_)





# The order of inheritance in multiple inheritance determines the Method Resolution Order (MRO).
# You can always check the MRO of a class using the help() function.
# The MRO helps avoid ambiguity when two or more parent classes define methods with the same name.