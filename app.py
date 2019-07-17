friends = ['ankit', 'bharti', 'rohit', 'bharti']
print(friends)
print(friends.count('bharti'))

print('\n')

print(f'index of bharti: {friends.index("bharti", 2)}')

friends.reverse()
print(friends)

print('\n')

friends_copy = friends.copy()
print(friends_copy)

print('\n')

friends.append('garima')
print(friends)

print('\n')

friends.insert(1, 'kailash')
print(friends)

print('\n')

friends.remove('bharti')
print(friends)

print('\n')

removed_name = friends.pop(1)
print(removed_name)
print(friends)

print('\n')

removed_name1 = friends.pop()
print(removed_name1)
print(friends)

print('\n')
friends.clear()
print(friends)

print('\n')
friends.append('ankit')
print(friends)

print('\n')

del friends[:]
print(friends)


square = list(map(lambda x: x ** 2, range(10)))
print(square)

greeing = lambda name: 'hello ' + name
print(greeing('ankit'))

addition = lambda value1, value2: value1 + value2
print(addition(2, 3))

friends.append('ankit')
friends.append('garima')
filtered_friends = list(filter(lambda name: name[0] == 'g', friends))
print(filtered_friends)

numbers = [0, 1, 2, 3, 4, 5]
transformed_numbers = list(map(lambda num: num + 1, numbers))
print(transformed_numbers)

