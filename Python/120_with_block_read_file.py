# with open automatically read and close the file...

# with block
# context manager

try:
    with open('textfile.txt', encoding='utf-8') as f:
        data = f.read()
        print(data)
except FileNotFoundError as err:
    print(err)
    print('The file you are looking is not exist. Please the file path.')