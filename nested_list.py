matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

print(matrix)

flatten_list = [[row[i] for row in matrix] for i in range(3)]
print(flatten_list)

_built_in_function = list(zip(*matrix))
print(_built_in_function)

del matrix[1:len(matrix)]
print(matrix)

#del matrix

# Tuple

http_errors = 404, 'File not found'
print(http_errors[0])
print(http_errors[1])

more_http_errors = http_errors, (808, 'connection error')
print(more_http_errors[1][0])

empty_tuple = ()
print(empty_tuple)

single_value_tuple = "name",
print(single_value_tuple)

a, b = http_errors
print(a, b)

# Set

_names = {'ankit', 'bharti', 'kailash'}
print(_names)

empty_names = set()
print(empty_names)
print('ankit' in _names)

a = set('abracadabra')
b = set('alacazam')

print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

# Dictionary
friends = {}
print(friends)

friends['ankit'] = 24
friends['rohit'] = 26

print(friends)
print('ankit' in friends)
print(list(friends))
del friends['ankit']
print(friends)

print("-------------------")

# Looping techinque

for key, value in friends.items():
    print(key, value)


for index, value in enumerate(reversed([1, 2, 3, 4, 5])):
    print(index, value)


import math

raw_data = [22.0, float('NaN'), 23.4, 43.32]
print(raw_data)
filtered_data = []

for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)


print(filtered_data)

def printFriends():
    print(matrix)


printFriends()