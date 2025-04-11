# advance min() and max()
 
# find the max lenght of the name 

def length_fun(item):
    return len(item)

print("FINDING MAX WITH NORMAL FUNCTION")

max_min_length = ['shubham','shashank','ashok','manish']
print(min(max_min_length, key = length_fun))# max length
print("FINDING MIN WITH NORMAL FUNCTION")
print(max(max_min_length, key = length_fun))#min length

# max() using with lambda annonmomus function 
print("FINDING MAX WITH LAMBDA FUNCTION")
print(max(max_min_length, key= lambda item : len(item)))


# find the maximum score of given ;

std_list_1 = [
    {'name':'shubham','score':90,'age':25},
    {'name':'aman','score':80,'age':23},
    {'name':'asish','score':74,'age':19}


]

score = (min(std_list_1, key = lambda items : items['score']))
print(score['name'], score['score'], score['age'])
# print(max(std_list_1, key = lambda item : item.get('name'))['score'])




# for i in std_list_1:
#     for key, value in i.items():
#         if (type(value) == int or type(value) == float):

#             print(max(value))