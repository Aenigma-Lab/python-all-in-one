#common method to delete data from list

# pop()---------------------->delete last element by default but if you pass the index number then it will delete that position element.

# del[] -----------------------> del is a operator it will delete element according to given index number.

# remove() ------------------> if you dont know the element position but know the name of element then by passing that element name it will remove the element from list
                                # if in the list have same name of two elements then it only remove first index occurance of that element.


#                        ########################     pop           ##################################
fruits = ["orange","apple","banana","grapes","kiwi"]
print(f"my original list is {fruits}")
fruits.pop() #by default it will delete last element, because not passed index number(kiwi)
print(f"i am deleting by default last element because you not passed index number {fruits}")
fruits.pop(1)# it will delete 1 index ele
print(f"i am deleting 1st index element because you mentioned the index number. {fruits}")


#                            #####################   del        ####################################

bag = ['pen','book','textbook','notebook']
del bag[2]
print(f"my bag having no textbook because index number 2 is deleted. current stuff in my bag is {bag}")


#                            #################    remove              #########################

building =["floor_1","floor_3","floor_8","floor_10","floor_2","floor_3"]
building.remove("floor_2")
print(f"It will remove floor_2 {building}")
building.remove("floor_3")
print(f"Here floor_3 having 2 time (dublicate of floor_3) it will only remove floor_2 first occure in index {building}")