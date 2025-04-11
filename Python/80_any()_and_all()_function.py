# all()
# any()


number_1 = [2,4,6,8,10]
number_2 = [1,2,3,4,5,6,6,7]

check = [True if i%2==0 else False for i in number_2]
print(check)
# output---- [True, True, True, True, True]

# if all number all even then it will print single True if any one number is odd it will print false
check_even_nums = [all(i for i in number_1)]
print(check_even_nums)

# any---- if all number is false and any one number is True it will print true

any_even = [any(i for i in number_2)]
print(any_even)
