# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature )
#################################################################################
#for doing simple task we have to do lot of work in data extraction
# here 'pandas' library come in picture. which is super useful to do 
#tabular data operation.
##########################################################################################
# pandas data for 1 dimension = series 
# pandas data in 2 dimension  = dataframe 
# series is like list in normal python 
import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
print(data["temp"])
# print data in dictionary
dict_data = data.to_dict()
#print data in list.
list_data =  data["temp"].to_list()

print(dict_data)
print(list_data)

#finding the average temperature.
temp_list = data["temp"].to_list()
print(len(temp_list))
avg_temp = sum(temp_list)/len(temp_list)
print(f"avg temp is {avg_temp}")

# in pandas we can do finding mean, median, mode, max, etc. temp
# this will give avg temp
print(data['temp'].mean())
print(data['temp'].median())
print(data['temp'].mode())
print(data['temp'].max())

# Get data in columns
print(data['condition'])
# and below is same as above 
print(data.condition)


#Get data in rows...
print(data[data.day == "Monday"])
#or we can write
print(data[data["day"] == "Monday"])

print(data[data.temp == data.temp.max()])

#own list to convert data in pandas
data_dict = {
    "name" : ['shubham','midhat','kiran','sana'],
    "roll_no":[100, 99, 98, 97]
}

data = pandas.DataFrame(data_dict)
print(data)
