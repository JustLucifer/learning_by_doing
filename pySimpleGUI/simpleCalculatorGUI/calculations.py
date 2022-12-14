def sub(x, y):
    return x - y


def add(x, y):
    return x + y


def multi(x, y):
    return x * y


def div(x, y):
    try:
        return round(x / y, 6)
    except ZeroDivisionError:
        pass


def calc(x:float | int, oper:str, y:float | int):
    if oper == '+':
        return add(x, y)
    elif oper == '-':
        return sub(x, y)
    elif oper == '*':
        return multi(x, y)
    elif oper == '/':
        return div(x, y)
