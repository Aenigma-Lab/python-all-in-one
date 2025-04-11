class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def phone_name(self):
        return f"{self.brand}{self.model}"

    # __str__ is used to define how the object should be represented as a string in a user-friendly way.
    # This method is meant to provide a simple, human-readable description of the object
    # when it is printed or converted to a string using str().
    def __str__(self):
        # This will be used when you call print(my_phone) or str(my_phone)
        # Example: 'Phone('Nokia', '1100', 1000) -> 'Nokia 1100, Price: 1000'
        return f'{self.brand} {self.model}, Price: {self.price}'
    
    # __repr__ is used to represent the object in a detailed way, primarily for debugging.
    # It should ideally return a string that can recreate the object using eval().
    # This method is useful when inspecting objects and debugging because it shows a complete 
    # description of the object and its attributes.
    def __repr__(self):
        # This will be used when you call repr(my_phone) or when the object is displayed
        # in a list, dictionary, or other collections.
        # Example: Phone('Nokia', '1100', 1000) -> "Phone('Nokia', '1100', 1000)"
        return f"Phone('{self.brand}', '{self.model}', {self.price})"
    

    def __len__(self):
        return len(self.phone_name())


# Creating instances of the Phone class
my_phone = Phone('Nokia', '1100', 1000)
print(len(my_phone))
# Example 1: Using __str__ via print
print("Using __str__ via print:")
# print(my_phone) will call the __str__ method, so this prints a user-friendly representation.
print(my_phone)  # This will print 'Nokia 1100, Price: 1000' because of the __str__ method.

# Example 2: Using __repr__ explicitly
print("\nUsing __repr__ explicitly:")
# Calling my_phone.__repr__() directly will return a more detailed string suitable for debugging.
print(my_phone.__repr__())  # This will print 'Phone('Nokia', '1100', 1000)'

# Example 3: Using __repr__ in a list
phones = [my_phone, Phone('Samsung', 'Galaxy S21', 1200), Phone('Apple', 'iPhone 14', 1500)]
print("\nUsing __repr__ for objects inside a list:")
# When we print a list of objects, each object uses __repr__ by default.
print(phones)  # This will print a list using __repr__, for each Phone object in the list.

# Example 4: Using __str__ in a list
print("\nUsing __str__ for objects inside a list:")
# We can loop over the list and print each object, which will use __str__ to show a user-friendly output.
for phone in phones:
    print(phone)  # This will call the __str__ method for each object in the list.

# Example 5: __repr__ and __str__ when printing a dictionary
phone_dict = {my_phone: "Old Nokia phone", phones[1]: "Modern Samsung", phones[2]: "Latest Apple phone"}
print("\nUsing __repr__ when the object is a key in a dictionary:")
# In a dictionary, the keys will use __repr__, while values use __str__ if defined.
print(phone_dict)  # Keys will use __repr__, values use __str__.

