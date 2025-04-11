#break and continue keyword

# 1 to 10 print
# break when i==5 so it will print till 4. only because it will break on 5 so it will not include 5.

for i in range(1,11):
    if i == 5:
        break
    print(i)


# for continue keyword.

# print 1 to 10 but not 5 use continue keyword.

for i in range(1,11):
    if i == 5:
        continue
    print(i)