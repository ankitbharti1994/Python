numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[-1])
print(numbers[0:2])
print(numbers[:])

float_value = 23.09783
print(round(float_value, 2))

name = 'ankit bharti'
formatted_string = f'My name is {name}'
print(formatted_string)
print(len(formatted_string))

multi_array = [['ankit', 'bharti', 'rohit'], [1, 2, 3]]
print(multi_array[0][2])

# fabonacci series

value = 5 * 6
val1 = 5
val2 = 6
print('multiplication of 5 and 6 is', value)
print(f'multiplication of {val1} and {val2} is {val1 * val2}')

a = int(input("enter value "))
if a < 0:
    a = 0
    print("Negative value set to", a)
elif a == 0:
    print(f"Value is {a}")
elif a > 0:
    print("More value")
else:
    print('other values')



numeric_range = range(2, 20)
for i in numeric_range:
    for v in range(2, i):
        if i % v == 0:
            print(f'{i} not a prime number')
            break
    else:
        print(f"{i} is a prime number")





for index in range(0, 4):
    print(index)
    if index == 3:
        break
else:
    print("Break didn't find")


def multiply(n):
    print(f'multiplication of {n} and 2 is {n * 2}')
    None

multiply(23)

def isVisible(num, by = 2):
    return num % by == 0

print(isVisible(10, 3))
print(isVisible(4, 2))

def doc():
    '''
        Do documentation.

        It's actually a documetation testing method
    :return: None
    '''

print(doc.__doc__)

def greeing(to: str, time: str = 'Good morning'):
    print(time + ' ' + to)

greeing('ankit')
print(greeing.__annotations__)