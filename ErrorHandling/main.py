try:  # Try to execute the line of code that may throw an error
    file = open('abc.txt')
    user = {"name": "ankit bharti"}
    print(user["name"])
except FileNotFoundError as error_message:  # Catch the error that may throw based on the code written in try block
    print(f'{error_message} not exist. So, creating new one.')
    file = open('abc.txt', 'w')
    file.write('something')
except KeyError as error_message:
    print(f"{error_message} key doesn't exist.")
else:  # Perform block of code if there is no error thrown in the try block
    contents = file.read()
    print(contents)
finally:  # Perform the final block of code like close file, no matter what happens in try block
    file.close()
    print('file closed')
