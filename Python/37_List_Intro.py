#data structure
#list ------------> this chapter

#ordered collection of items

#You can store anything in List ,in , float, string.


number_list = [1,2,3,4]
print(number_list)


words = ['word1','word2','word3']#we can print words also

print(words)
print(words[:1])# it will print index 0
print(words[:2])# it will print index 0 and 1 means word1 and word2

print(words[0][0])# if you want to access the first index first letter.

mixed = [1, 2, 3, 4, "five", "six", 2.3, None
] # None means(kuch nahi)

print(mixed)
print(mixed[-1])# it will access last index.


# if we want to change the value of mixed list of index 1.
mixed[1] = 3
print(mixed)

mixed[2:] = 'two' #index number start with index 2 till last replace all with 'two' with one one letter.
# output::::::: [1, 3, 't', 'w', 'o']
print(mixed)
