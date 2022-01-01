import csv
import pandas

def readCSV():
    with open("weather_data.csv") as file:
        data = csv.reader(file)
        temperatures = []
        for row in data:
            temperature = row[1]
            if temperature != 'temp':
                temperatures.append(int(temperature))
            else:
                pass

        print(temperatures)


data = pandas.read_csv('weather_data.csv')
average = data['temp'].mean()
print(average)

max_temp = data['temp'].max()
print(max_temp)

print(data.condition)
print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
print(monday.temp)


dict = {
    'students': ['ankit', 'garima', 'rohit'],
    'marks': [40, 50, 30],
}

dataframe = pandas.DataFrame(dict)
print(dataframe)
dataframe.to_csv('new_data.csv')
