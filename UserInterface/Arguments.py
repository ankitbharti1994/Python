def add(*values: int | float) -> int | float:
    return sum(values)


def calculate(n: int, **kwargs) -> int:
    name = kwargs.get('name')
    if not name:
        print('Name is missing')

    for key, value in kwargs.items():
        if key == 'add' and type(value) is int:
            n += value
        elif key == 'multiply' and type(value) is int:
            n *= value
        elif key == 'subtract' and type(value) is int:
            n -= value
        elif key == 'divide' and type(value) is int:
            n /= value

    return n


if __name__ == '__main__':
    print(add(2, 3, 4, 1, 8))
    print(add(2, 4, 4))
    print(add(2.5, 4, 2.6))
    print(calculate(3, add=3, multiply=5))
