class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @name.deleter
    def name(self):
        del self._name


user = User('ankit')
print(user.name)
user.name = 'ankit bharti'
print(user.name)
del user.name


value = int(input('enter number: ').strip())
# print(value)
#
# if value % 2 == 0:
#     if value in range(2, 6):
#         print('Not Weird')
#     elif value in range(6, 21):
#         print('Weird')
#     elif value > 20:
#         print('Not Weird')
# else:
#     print('Weird')
#
#
# a = int(input('first number: '))
# b = int(input('second number: '))
#
#
# inputs = [a, b]
# print(sum(inputs))
# print(a - b)
# print(a * b)
#
# print(a // b)
# print(a / b)

# updated_list = [n ** 2 for n in range(0, value)]
# for number in updated_list:
#     print(number)

# def is_leap(year):
#     leap = False
#
#     # Write your logic here
#     if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#         leap = True
#     elif year % 4 == 0 and year % 100 == 0 and year % 400 > 0:
#         leap = False
#     elif year % 4 == 0:
#         leap = True
#
#     return leap
#
#
# year = int(input('enter year: '))
# print(is_leap(year))

updated_list = [str(n) for n in range(1, value + 1)]
data = ''
for number in updated_list:
    data += number

print(data)
