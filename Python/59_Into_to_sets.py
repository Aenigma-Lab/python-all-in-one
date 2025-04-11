# set is unordered collection of unique items
# set does not have indexing.
# set only contain unique items.


# we can not store list dictionary and tuple in sets.


# set having methods like
# 1. add()---> add element in set
# 2. remove()----> remove element in set.
# 3. discard()----->if you want to remove element which is not in set you can use discard insted of 
    # remove because remove will give error and discard will not give error if you discard those element which is not present in set.
# 4. clear()---> to clear the set
# 5. copy()---> use to copy set

s = {1,2,2,3}
print(s)

# print(s[1])# ❌ not support indexing

# suppose you have list and you want to remove dublicate
# we can remove dublicate using set and then convert to list.

list1 = [1,2,3,4,5,5,6,6,1,2,8]
unique_item = set(list1)
final_list = list(unique_item)
print(final_list)


set1 = {1,2,3}
set1.add(1)#❌ here 1 will not added becuase it having unique element only
set1.remove(1)
print(f"after removing the 1 elemnt {set1}")
#  set1.remove(8)#❌ this will give error element not present
set1.discard(8)# ✅ if element is not present it will not give erorr and if element is present then it will remove

print(set1)




################# set data storing type ##########

set2 = {1,1.0,1.1,'string',2}
print(set2) # here 1 and 1.0 is same it will not print dublicates