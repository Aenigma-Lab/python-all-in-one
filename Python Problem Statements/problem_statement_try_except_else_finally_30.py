# make a function 'divide'
# divide(a,b)

# print(divide(4,2)) # 2
# print(divide(4,0)) #please don't divide by zero, zero 
# print(divide('4',2)) # please input numbers only. 

# simple method 

def divides(c,d):
    try:
        return c/d
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print("Please put value in int or float only.")
    
    except:
        print("INVALID ERROR!!")


print(divides(10,3))







# def divide(a, b):
#     try:
#         # Check if inputs are numbers
#         if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#             return "Please input numbers only."
#         # Check if b is zero
#         if b == 0:
#             return "Please don't divide by zero."
#         return a / b
#     except Exception as e:
#         return f"An unexpected error occurred: {str(e)}"

# # Example Usage
# print(divide(4, 2))    # Output: 2
# print(divide(4, 0))    # Output: Please don't divide by zero.
# print(divide('4', 2))  # Output: Please input numbers only.

# # Taking user input
# try:
#     a, b = map(float, input("Division: Enter Numerator and Denominator, separated by a comma: ").split(','))
#     print(divide(a, b))
# except ValueError:
#     print("Invalid input! Please enter numbers separated by a comma.")
