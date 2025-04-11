# Here we compare list and array.....
# strings are immutable--->onece created can not changeh your string.

# list are mutable ------> we can add delete and modify the element in the list.


name = "shubham"  #---------->string

title = name.title()# this will create another string.
print(f"New sting will create for title() {title}")# 
print(f"Original string is {name}")# this original string will not chnage.

########################################################
####################    LIST        ####################
building = ["floor_1","floor_2","floor_3"]#-------->list

building.pop()#it will remove last element from list. This chnages will happen in original string.
print(f"After pop() {building}")

building.append("ground_floor")# this will add "ground floor" on Zero'th index.
print(f"After append() {building}")

building.insert(0,"floor_8")
print(f"After insert() method {building}")


# So the main difference is in string and list is "changes can not happen in string but changes can be done in list."




