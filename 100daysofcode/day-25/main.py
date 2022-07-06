# with open("226 weather-data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("226 weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#         print(temperatures)

import pandas

data = pandas.read_csv("226 weather-data.csv")
# print(data['temp'])

data_dict = data.to_dict()
# print(data_dict)

temp_list = data['temp'].to_list()
# print(len(temp_list))

# avg_temp = sum(temp_list) / len(temp_list)
avg_temp = data['temp'].mean()
# print(avg_temp)

# print(data[data['temp'] == data.temp.max()])
monday = data[data.day == 'Monday']
'''Get Monday's temp and convert to Fahrenheit'''
print(int(monday.temp) * 9/5 + 32)

'''Create a Dataframe'''
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")