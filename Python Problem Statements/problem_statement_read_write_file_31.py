# # exercise

# with open('salary.txt','r+') as read_salary:
#     with open('propersalary.txt','r+') as write_salary:
#         for usr_sal in read_salary:
#             write_salary.write(usr_sal.read())



with open('salary.txt','r') as read_salary:
    with open('propersalary.txt','a') as write_salary:
        for line in read_salary.readlines():
           name, salary = line.split(',')
           write_salary.write(f"{name} salary is {salary}")