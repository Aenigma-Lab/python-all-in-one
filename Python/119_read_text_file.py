# readfile
# open function
# read method -- for reading file
# seek method----- to change the cursor position ex my cursor present position at 210 word but we can change to 251 
# tell method--- it tell current position of cursor
# readline method---- it read one line at a time
# readlines method --- it will add all lines in one list []
# close method


f = open('file.txt','r')
print(f'cursor position - {f.tell()}')
print(f.readline(), end = " ") # it read only one line end = '' it will remove empty spaces
print(f.read())
print(f'cursor position - {f.tell()}') # tell method tell what is current position of cursor
print('before seek method cursor position')
f.seek(10)
print('after seek method cursor position')

print(f'current position of cursor position - {f.tell()}')

lines = f.readlines()
print(lines)
print(len(lines)) #finding the length of lines
# looping of lines
for line in lines:
    print(line)

# check file name using it is called data decryptor #name #

f.close()