# import csv
#
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

# import pandas
#
# data = pandas.read_csv('weather_data.csv')
# temp_list = data['temp'].to_list()
# # max_temp = data['temp'].max()
# # print(data[data.temp == max_temp])
#
# monday = data[data.day == 'Monday']
# monday_temp = monday.temp
# temp_in_f = monday_temp * 9/5 + 32
# print(temp_in_f)

import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_data = data['Primary Fur Color'].to_list()
fur_dic = {
    'fur_color': ['Gray', 'Cinnamon', 'Black'],
    'fur_count': [0,0,0],
}

for fur_color in fur_data:
    if fur_color in fur_dic['fur_color']:
        index = fur_dic['fur_color'].index(fur_color)
        fur_dic['fur_count'][index] += 1


fur_count_data = pandas.DataFrame(fur_dic)
print(fur_count_data)
fur_count_data.to_csv('squirrel_count.csv')

