# Static Method Example in Python
# Static Method in Python
    # A static method is a method that is bound to the class, rather than to an instance of the class.
    # This means it does not have access to the instance (self) or the class (cls) itself.
    # It is used when you need a method that performs some operation but does not require access 
    # to any instance or class-specific data. Static methods are defined using the @staticmethod decorator.
    


class Calculator:
    # Static method: This method doesn't require the instance (self) or class (cls) to work.
    # It only performs operations on the provided arguments.
    @staticmethod
    def hello_static():
        print("this is static method.")
    @staticmethod
    def add(a, b):
        # Performs addition of two numbers and returns the result
        return a + b
    
    @staticmethod
    def subtract(a, b):
        # Performs subtraction of two numbers and returns the result
        return a - b

    @staticmethod
    def multiply(a, b):
        # Performs multiplication of two numbers and returns the result
        return a * b

    @staticmethod
    def divide(a, b):
        # Performs division of two numbers and returns the result
        # If b is zero, it will return 'Undefined' as division by zero is not allowed
        if b == 0:
            return "Undefined (cannot divide by zero)"
        return a / b

# Calling static methods directly using the class name
# Static methods can be called using the class name without needing to create an instance.
print(Calculator.hello_static())
print("Addition:", Calculator.add(10, 5))        # 10 + 5 = 15
print("Subtraction:", Calculator.subtract(10, 5))  # 10 - 5 = 5
print("Multiplication:", Calculator.multiply(10, 5))  # 10 * 5 = 50
print("Division:", Calculator.divide(10, 5))      # 10 / 5 = 2.0
print("Division by Zero:", Calculator.divide(10, 0))  # Undefined (cannot divide by zero)


# Static methods can also be called on an instance, though this is not recommended.
# It's better to use them directly from the class to clarify their nature as independent methods.

calc = Calculator()  # Creating an instance of the Calculator class
print("Addition using instance:", calc.add(100, 50))  # 100 + 50 = 150


# Explanation and Summary of Static Methods:

# 1. **What is a static method?**
#    - A static method is a method that belongs to the class rather than the instance of the class.
#    - It does not require access to the instance (self) or class (cls) variables.
#    - Static methods are defined with the `@staticmethod` decorator.

# 2. **When to use static methods?**
#    - Use static methods when you need functionality related to the class but that doesn't require access to the instance or class-specific data.
#    - It's useful for utility functions that don't modify or rely on object or class state.

# 3. **How to call static methods?**
#    - Static methods can be called directly on the class (`Calculator.add()`) or on an instance (`calc.add()`).
#    - However, calling static methods from the class is recommended because it clarifies that the method does not interact with instance or class data.

# 4. **Advantages of static methods:**
#    - Static methods make code cleaner and more organized by grouping utility functions inside a class.
#    - They allow functions to be used without the need to create an instance of the class.
#    - They do not modify the state of the class or instance, which keeps them independent and reusable.
