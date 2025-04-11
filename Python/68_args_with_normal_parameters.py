#args with normal parameters
# The *args syntax allows you to pass a variable number of positional arguments to a function. Here's an example using different functions to illustrate how *args can be used in various contexts, along with explanations for each.

def multiply_nums(num1, *args):
    print(f"this is not the part of args {num1}")
    print(f"args arguments is {args}")
    multiply = 1
    for i in args:
        multiply *=i
    return multiply
print(multiply_nums(2,4,5))


# Using *args to accept variable-length arguments

# 1. Sum of Numbers
def sum_nums(num1, *args):
    print(f"This is the first parameter: {num1}")
    print(f"Additional arguments: {args}")
    total = sum(args)
    return total

# Example usage
print(sum_nums(10, 1, 2, 3, 4))  # Outputs: 20

# 2. Concatenating Strings
def concatenate_strings(prefix, *args):
    print(f"Prefix: {prefix}")
    print(f"Strings to concatenate: {args}")
    result = ' '.join(args)
    return f"{prefix} {result}"

# Example usage
print(concatenate_strings("Hello", "World", "from", "ChatGPT!"))  # Outputs: "Hello World from ChatGPT!"

# 3. Finding Maximum Value
def find_max(num1, *args):
    print(f"Initial value: {num1}")
    print(f"Additional values: {args}")
    max_value = max(args, default=num1)
    return max(num1, max_value)

# Example usage
print(find_max(5, 10, 3, 8))  # Outputs: 10

# 4. Creating a Custom Greeting
def custom_greeting(greeting, *names):
    print(f"Greeting message: {greeting}")
    print(f"Names to greet: {names}")
    greetings = [f"{greeting}, {name}!" for name in names]
    return greetings

# Example usage
print(custom_greeting("Hello", "Alice", "Bob", "Charlie"))  
# Outputs: ["Hello, Alice!", "Hello, Bob!", "Hello, Charlie!"]

# 5. Calculating Average
def calculate_average(initial_value, *args):
    print(f"Initial value: {initial_value}")
    print(f"Numbers for average: {args}")
    if args:
        average = (initial_value + sum(args)) / (1 + len(args))
    else:
        average = initial_value
    return average

# Example usage
print(calculate_average(10, 20, 30, 40))  # Outputs: 25.0

# 6. Merging Dictionaries
def merge_dicts(initial_dict, *args):
    print(f"Initial dictionary: {initial_dict}")
    merged_dict = initial_dict.copy()
    for arg in args:
        print(f"Merging with: {arg}")
        merged_dict.update(arg)
    return merged_dict

# Example usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dicts(dict1, dict2, {'d': 5}))  # Outputs: {'a': 1, 'b': 3, 'c': 4, 'd': 5}
