#Looping in List...........

my_bag = ['pen','pencil','books','notebooks','geometorybox','tiffin','purse']

# using  for loop::::::::
for stuff in  my_bag:
  print(stuff)


print("End for loop:::::::::::::::::::: \n\n\n")



# using while loop:::::::
print("Start while loop::::::::::::::::")
stuf = 0
my_bag_len = len(my_bag)
print(type(my_bag_len))
while (stuf) < my_bag_len:
  bag = my_bag[stuf]
  print(bag)
  stuf+=1