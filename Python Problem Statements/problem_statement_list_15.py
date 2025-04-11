#define a function which will take list as a argument and this function will returen a reverse list.

# example
# [1,2,3,4] ------> [4,3,2,1]

# ['word1','word2','word3',]------> ['word3','word2','word1']

# Note you simply do this with reverse method or [::-1]

# but try to do this with the help of append() and pop() method.

#___________________________________________________________________________________________
#using first simple first method [::-1]
word_list = ['word1','word2','word3','word4','word5']

def rev_list(word_list):
 return word_list[::-1]    
print(rev_list(word_list))


#using second method push() and pop().
num_list = ['one','two','three','four','five']
rev_order =[]
len_num_list = len(num_list)
def reverse_list(num_list):
  num = 0
  print("using pop() and pursh() method to reverse list.")
  for num in range(len_num_list):
    if num < len_num_list:
      poped_element = num_list.pop()
      rev_order.append(poped_element)
reverse_list(num_list)
print(rev_order)


#___________________________________________________________________________________________
# we can also use reverse method:
list = [1,2,3,4,5]
list.reverse()
print(f"reversing list using reverse() method{list}")


#___________________________________________________________________________________________
# another one method is 

l = [1,2,3]
def rev(l):
  r_list = []
  for i in range(len(l)):
    popped_item = l.pop()
    r_list.append(popped_item)
  return r_list
output = rev(l)

print(f"Another simple method for reverse{output}")
