from nested_list import printFriends as friends

names = ['ankit', 'bharti', 'amit']

filterd_names = filter(lambda name: len(name) > 5, names)
filterd_names1 = list([name for name in names if len(name) > 5])
print(list(filterd_names))
print(filterd_names1)

friends()