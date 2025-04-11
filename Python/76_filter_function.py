# filter function ....
# Explanation of the filter function

# The filter() function constructs an iterator from elements of an iterable for which a function returns true.
# The syntax is:
# filter(function, iterable)

# If the function returns True for an element, that element is included in the output; otherwise, it is excluded.

# Example 1: Filtering even numbers from a list using a normal method
numbers = [1, 2, 3, 4, 5, 6]

# Normal function to filter even numbers
def is_even(n):
    return n % 2 == 0

# Manually filtering even numbers using a loop
even_numbers_manual = []
for number in numbers:
    if is_even(number):
        even_numbers_manual.append(number)

print("Even numbers (manual):", even_numbers_manual)  # Output: [2, 4, 6]


# Example 2: Using the filter function to achieve the same result
# Using the filter function with the is_even function
even_numbers_filter = list(filter(is_even, numbers))
print("Even numbers (filter):", even_numbers_filter)  # Output: [2, 4, 6]


# Example 3: Filtering odd numbers using a lambda function
# This example demonstrates how to filter odd numbers using a lambda function with filter()
odd_numbers_filter = list(filter(lambda n: n % 2 != 0, numbers))
print("Odd numbers (filter with lambda):", odd_numbers_filter)  # Output: [1, 3, 5]


# Example 4: Filtering strings by length
# List of strings
words = ["hello", "world", "python", "is", "awesome"]

# Function to filter words longer than 3 characters
def long_words(word):
    return len(word) > 3

# Using filter to get words longer than 3 characters
filtered_words = list(filter(long_words, words))
print("Words longer than 3 characters:", filtered_words)  # Output: ['hello', 'world', 'python', 'awesome']


# Example 5: Using filter with multiple criteria
# Filtering numbers greater than 5 and even
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Function to check if a number is greater than 5 and even
def is_greater_than_five_and_even(n):
    return n > 5 and n % 2 == 0

# Using filter to apply the function
filtered_numbers = list(filter(is_greater_than_five_and_even, numbers2))
print("Numbers greater than 5 and even:", filtered_numbers)  # Output: [6, 8, 10]


# Example 6: Advanced example - Filtering out non-positive numbers
numbers3 = [-10, -5, 0, 5, 10, 15]

# Using filter to keep only positive numbers
positive_numbers = list(filter(lambda x: x > 0, numbers3))
print("Positive numbers:", positive_numbers)  # Output: [5, 10, 15]


# Example 7: Filtering out None values from a list
mixed_values = [1, 2, None, 3, None, 4]

# Using filter to remove None values
filtered_values = list(filter(lambda x: x is not None, mixed_values))
print("Values without None:", filtered_values)  # Output: [1, 2, 3, 4]
