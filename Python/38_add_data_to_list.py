# how to add items to our list
# most common thing that you can do with list and most imp

fruit_basket = ['grapes','apple']
fruit_basket.append("mango")# always item will added in last and it will take one argument.
print(f"In my basket have {fruit_basket}")


#In real life project you dont know how many can be in your list then you simply create a black list and you will append items.
# using this we can store data in list.



# METHODS TO ADD DATA IN LIST:::::::::::::::::::::::::::::::::::::::::
# append()------------------------> add element last in the list. if you  append a list (whole list will extend).

# insert()------------------------> add any element at any position in the list.

# join(concatenate)----------------> add two list 

# extend()--------------------------> list2 all elements will added to list2, so it will create single list.

#                  #############################        append        #################
bag = []
bag.append("book")
bag.append("notebook")
print(f"my bag currently having {bag}")


#                 ##################################      insert       ######################
building = ["floor1","floor3","floor4"]
building.insert(1,"floor2")#here floor2 inserted in building at index position 1.
building.insert(10,"floor5")#this index is not present in the list so element will add in last index.
print(f"my building floors are {building}")


#                        ##################################  concatenate ####################
floor_1 = ["room_1","room_3"]
floor_2 = ["room_2","room_4","room_5"]
all_floors = floor_1 + floor_2
print(f"In my home floors are {all_floors}")


#                     ###############################   extends ###########################

bag_1 = ["pen","book","pencil"]
bag_2 =["tiffin","diary"]
bag_1.extend(bag_2)
print(f"only bag_2 stuff will shift in bag_1 {bag_1} but bag_2 remain shame {bag_2}")

##### V.V IMP
print("Using append method whole list will append with the list. we can say list inside list.")
bag_1.append(bag_2)   
print(f"here the whole bag with item append (inside) bag_ 1 {bag_1}")                      #####       
#####

