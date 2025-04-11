# basic sorting 
# list sorting 
fruits = ['graps','mango','apple']
#sorting list we can write this
fruits.sort()
print(fruits)

#tuple sorting
fruits_2 = ('gapes','mango','apple')
print(f"Here tuple sort and it will return list {sorted(fruits_2)}")
print(f"it will not sort because tuples are mutable {fruits_2}")

# sets sorting 
fruits_3 = {'graes','mango','apple'}
print(f"it short set and return a list {sorted(fruits)}")


#Advance sorting 

laptops = [
    {'model': 'Dell XPS 13', 'price': 999.99},
    {'model': 'Apple MacBook Air', 'price': 1199.00},
    {'model': 'HP Spectre x360', 'price': 1299.99},
    {'model': 'Lenovo ThinkPad X1 Carbon', 'price': 1399.99},
    {'model': 'Asus ROG Zephyrus G14', 'price': 1499.99},
    {'model': 'Microsoft Surface Laptop 4', 'price': 999.99}
]

price_sorting = [sorted(laptops, key= lambda item : item['price'], reverse=True)]
print(price_sorting)