# we can write csv file using 
# writer
# DictWrite
from csv import writer
with open('file2.csv','w', newline='') as write_csv:
    csv_write = writer(write_csv) 

    csv_write.writerow(['name','state'])
    csv_write.writerow(['Shubham','Maharashtra'])
    csv_write.writerow(['Sumit','Delhi'])


    # we can write with multiple list also...
    csv_write.writerow([['manish','Bihar'],['Ashish','Patna']])

# using DicWrite method...................

from csv import DictWriter
with open('file2.csv','w',newline='') as write_csv:
    csv_writer = DictWriter(write_csv,fieldnames=[f'firstname','lastname','age'])
    csv_writer.writeheader()

    # we can write using----> writerow, writerows 
    csv_writer.writerow({
        'firstname': 'sumit', 
        'lastname': 'kumar',
         'age' : 35 
        })
    csv_writer.writerow({ 
        'firstname': 'ramesh', 
        'lastname': 'sudhaker',
         'age' : 46 
         })
    

    csv_writer.writerows([{'firstname': 'sumit', 'lastname': 'kumar','age' : 35 },
         {'firstname' : 'manish','lastname':'jaiswal','age' : 30},
         {'firstname': 'sachin', 'lastname' : 'tendulkar' ,'age' : 40}
    ])