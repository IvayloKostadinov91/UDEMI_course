def add(n1, n2):
    return n1 + n2


def substact(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(n1, n2, func):
    return func(n1, n2)


print(calculator(n2 = 10, n1 = 220, func = divide))
