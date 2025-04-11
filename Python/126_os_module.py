import os

# print(os.getcwd()) ### check current working directory
# os.mkdir('movies') ### make folder

# os.rmdir('movies') ###  remove the folder  movies

# print(os.path.exists('movies')) ## it return False if not existe the path or folder , it return True if the path is exists.


if os.path.exists('test_folder'):
    print('already exists')
# else:
#     os.mkdir('test_folder')## if not exists then create folder.


#creating and closing file directly in append mode....
# open('new_file.txt','a').close()

# it will give list of file and folders
print(os.listdir())

# os.chdir(r'D:\shubham\'newfolder')
# print(os.listdir())

#direct inside the directory or files.......

fileiter = os.walk(r'/home/alfa')
for current_path, folder_name, file_name in fileiter:
    print(f'current path :{current_path}')
    print(f'folder name :{folder_name}')
    print(f'file names :{file_name}')


