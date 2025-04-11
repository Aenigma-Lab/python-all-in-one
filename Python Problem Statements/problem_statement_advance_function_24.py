# Challenge.
"""
Question:
Write a function that takes any number of lists containing numbers and returns 
the average of the corresponding elements from each list. 

For example, given the lists [1, 2, 3], [4, 5, 6], and [7, 8, 9], the function 
should return the averages: 

(1 + 4 + 7) / 3, (2 + 5 + 8) / 3, (3 + 6 + 9) / 3
which results in the output: [4.0, 5.0, 6.0]
"""

# try to make this anonymous function in one line using lambda 
avg = []
def find_avg(list_1, list_2, list_3):
    for pair in zip(list_1,list_2, list_3):
        avg.append(sum(pair)/len(pair))
    return avg

print(f"avg using zip funct {find_avg([1,2,3],[4,5,6],[7,8,9])}")


#another way we can write this using *args
avg = []
def find_avgs(*args):
    for pair in zip(*args):
        avg.append(sum(pair)/len(pair))
    return avg

print(f"avg with *args {find_avgs([1,2,3],[4,5,6],[7,8,9])}")


# another way to write with lambda function...
avg_with_lambda_func = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
print(f"average with lambda function {avg_with_lambda_func([1,2,3],[4,5,6],[7,8,9])}")



