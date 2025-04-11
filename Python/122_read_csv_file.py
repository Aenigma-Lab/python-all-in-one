
#reading csv file using reader method.
from csv import reader
with open('file.csv', 'r') as csv:
    csv_read = reader(csv)
    print(type(csv_read))# this is iterator
    next(csv_read)# this is iterator it loop only once.
    for row in csv_read:
        print(row)
    for row in csv_read:
        print(row)

