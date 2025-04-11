from csv import DictReader

with open('file2.csv','r') as csv:
    csv_read = DictReader(csv, delimiter='|') # we have to pass the delimiter if we are using diffrent symbole insted of comma(,) in csv file.
    print(type(csv_read))

    for row in csv_read:
        print(row)


# we can also print name only email only 
    # for row in csv_read:
    #     print(row['email'])