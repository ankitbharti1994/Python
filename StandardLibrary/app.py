import os
import pandas as pd

print(os.getcwd())
os.chdir('/Users/ankitkumarbharti/Desktop/Practice/Python/StandardLibrary/')

print(os.getcwd())
data = pd.read_csv('Simple.csv')
print(data)

print('------------------------------\n')

print(data)

print('-------------------------------\n')

data['Sum'] = data.X + data.Y + data.Z
data['Subtraction'] = data.X - data.Y - data.Z
data['Multiplication'] = (data.X * data.Y * data.Z) ** 2
print(data)

data.to_csv('Something.csv')

data = data.drop('Subtraction', axis=1)
print(data)

print('-----------------------\n')

Filter = data.Multiplication < 1000

print(data[Filter])