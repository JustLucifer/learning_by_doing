def sub(x, y):
    return x - y


def add(x, y):
    return x + y


def multi(x, y):
    return x * y


def div(x, y):
    return x / y


def calculation(x, oper, y):
    if oper == '+':
        return add(x, y)
    elif oper == '-':
        return sub(x, y)
    elif oper == '*':
        return multi(x, y)
    elif oper == '/':
        return div(x, y)
