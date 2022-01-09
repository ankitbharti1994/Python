def cuboid_volume(number):
    if type(number) not in [int, float]:
        raise TypeError('The length of cuboid can only be a valid integer or a float')
    return number * number * number


def add(n1: int, n2: int) -> int:
    if type(n1) not in [int, float] or type(n2) not in [int, float]:
        raise TypeError('Given value is not a valid integer or float')
    return sum([n1, n2])


def greeting(name: str) -> str:
    return 'Hello {0}'.format(name)