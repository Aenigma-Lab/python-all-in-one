# Exception Handling 
# try except else finally
while True:
    try:
        age  = int(input('enter your age: '))
        break
    except ValueError:
        print('may be you enter age in  text, please input age in  number.')
    except:
        print('invalid input.......')

if age < 18 :
    print('You can\'t play this game.')
else: 
    print('you can play this game.')