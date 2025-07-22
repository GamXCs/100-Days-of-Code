# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
from lib2to3.pytree import convert
from operator import length_hint

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = [] #extract temps from csv as an int
#
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
from pandas.core.internals.construction import dataclasses_to_dicts

#Pandas library handles reading data much better
data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data['temp']))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].tolist()
# length = (len(temp_list))
# list_avg = sum(temp_list) / length
# print(list_avg)

"""Instead of using typical Py code, I can use features from Pandas API"""
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data["condition"])
# print(data.condition)

# Get data from the Rows by getting the entire data set, calling the column and
# searching for the specific initial key
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

# Can get data from a specific day by placing it in a variable
monday = data[data.day == 'Monday']
print(monday.temp)

# Convert monday's temp into Fahrenheit
cels_conversion = (monday.temp * 1.8) + 32
print(cels_conversion)

"""Create a dataframe from scratch by calling pandas.DataFrame and passing the dictionary 
"""
data_dict = {
    "students":['Amy','James','Angela'],
    "scores":[76,54,65]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("new_data_list") #can convert to csv using pandas library