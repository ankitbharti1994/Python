friends = ['ankit', 'bharti', 'garima']
print(friends)

friends.append('rohit')
print(friends)

friends[len(friends):] = ['kailash']
print(friends)

friends.insert(1, 'sumit')
print(friends)

removed_friends = friends.remove('bharti')
print(removed_friends)

friends.clear()
print(friends)

def multiply(num):
	return lambda x: x * num

value10 = multiply(10)
print(value10(9))

print(value10(20))


print(x**2 for x in range(10))
print([x**2 for x in range(10)])

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

numbers = [-1, 2, 3, -4, 5, -6]
print([x for x in numbers if x > 0])

print([abs(x) for x in numbers])

names = [' ankit   ', 'bharti', '   kailash']
print([name.strip() for name in names])

names = ['  ankit bhaerti  ', 'bharti  ', '  garima', '  kailash   ']
print([name.strip() for name in names])