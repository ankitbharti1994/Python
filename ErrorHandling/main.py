def error_handling():
    """
    Use `try, except, else and finally` method to handle the error handling in python.

    There can be multiple `except` block if try can throw more than one different type of error.

    - try: Try to execute the line of code that may throw an error.
    - except: Cath the error that may throw based on the code written in try block.
    - else: Perform block of code if there is no error thrown in the try block.
    - finally: Perform the final block of code like close file, no matter what happens in try block.
    """
    try:
        file = open('abc.txt')  # Here trying to open a file which may not be available
        user = {"name": "ankit bharti"}
        print(user["name"])  # Trying to access the value by key but key may not be available
    except FileNotFoundError as error_message:
        # Use `as <message>` to get the message associated with the error
        print(f'{error_message} not exist. So, creating new one.')
        file = open('abc.txt', 'w')
        file.write('something')
    except KeyError as error_message:
        print(f"{error_message} key doesn't exist.")
    else:
        contents = file.read()
        print(contents)
    finally:
        file.close()
        print('file closed successfully')


def raise_error():
    height = float(input('Height: '))
    if height > 3:
        raise ValueError('Human height should not be over 3 meters.')

    weight = int(input('Weight: '))

    bmi = weight / height ** 2
    print(f'BMI: {bmi}')


error_handling()

try:
    raise_error()
except ValueError as message:
    print(message)


fruits = ['Apple', 'Pear', 'Orange']


def make_pie(index: int):
    try:
        fruit = fruits[index]
    except IndexError as error:
        print(error)
    else:
        print(f'{fruit} pie')


make_pie(int(input('Enter index: ')))

