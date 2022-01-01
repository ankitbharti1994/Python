def divide(num1, num2):
    return num1 / num2

try:
    result = divide(5, 1)
except ZeroDivisionError:
    print('tried to divide using 0')
    raise
else:
    print(f'result is {result}')
finally:
    print('executing finally clause')