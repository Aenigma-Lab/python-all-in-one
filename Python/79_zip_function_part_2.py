list_1 = [1,3,5,7]
list_2 = [2,4,6,8]
# if we use zip funcion 
print(list(zip(list_1,list_2)))
# output  [(1, 2), (3, 4), (5, 6), (7, 8)]

# but we want to do reverse using zip funcion ouput we have to make 2 lists 

# -----------------using * operator with zip---------------------
final_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(list(zip(*final_list)))
# unzip the tuples in seprate list 
first_list, second_list = list(zip(*final_list))
print(list(first_list)) #converting in list
print(second_list) # keeping by default in (tuple)


# from the pair [(1, 2), (3, 4), (5, 6), (7, 8)]  find biggest number using zip
# like from (1,2) 2 is greater
max_list = []
for pair in zip(list_1,list_2):
   
    max_list.append(max(pair))
print(f"max number form pair is {max_list}")

