fabonacci_cache = {0: 0, 1: 1}


def fabonacci(value: int) -> int:
    if value <= 1:
        return fabonacci_cache[value]
    else:
        # f(2) = f(1) + f(0) // 1 + 0 = 1
        # f(3) = f(2) + f(1) // 1 + 1 = 2
        # f(4) = f(3) + f(2) // 2 + 1 = 3
        for i in range(2, value + 1):
            try:
                fabonacci_cache[i]
            except KeyError:
                new_value = fabonacci(i - 1) + fabonacci(i - 2)
                fabonacci_cache[i] = new_value

        return fabonacci_cache[value]


print(fabonacci(int(input('Enter desired number: '))))
