
#lambda expression practicle

def is_even(a):
    if a%2 == 0:
        return True
    return False
print(is_even(10))


#Another example

#Lambda with If Else ........
s = 'hello0'

func = lambda s : "Sahi h" if len(s) > 5 else False
print(func(s))


# Make short of above example.....


func2 = lambda s : len(s) > 7
print(func2(s))


#Another one is 

def last_char(s):
    return s[-1]


print(last_char("Shubham"))
 # Make short the above example:

last_chars = lambda s : s[-1]
print(last_chars("Mishra"))