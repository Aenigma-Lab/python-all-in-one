# Exception Handeling 
# part 2
# else and finally 
while True:
    try:
        age = int(input('Enter your age. '))
    except ValueError:
        print('Plese enter age in number, may be you enterd in text.')

    except:
        print('Invalid Input !!')

    else:
        print(f'you have enter {age}')
        break # we use here insted of try block
    finally:  # this will run at any condition....
        print('This is finally block this must be run at any condtion')
        