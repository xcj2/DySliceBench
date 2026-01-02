def calc(a, b, op):
    """
    a: int
    b: int
    op: operator
    returns the result of arithmetic operation

    >>> calc(1, 2, '+')
    3
    >>> calc(56, 18, '-')
    38
    >>> calc(13, 2, '*')
    26
    >>> calc(100, 10, '/')
    10
    >>> calc(27, 81, '+')
    108
    """
    def add(a, b):
        return a + b
    def sub(a, b):
        return a - b
    def prod(a, b):
        return a * b
    def div(a, b):
        return a // b

    operators = {
        '+': add,
        '-': sub,
        '*': prod,
        '/': div,
    }

    if op in operators:
        return operators[op](a, b)

    raise Exception('invalid operator')


if __name__ == '__main__':

    while True:
        cmd = input().split(' ')
        (a, op, b) = (int(cmd[0]), cmd[1], int(cmd[2]))
        if op == '?':
            break
        print(calc(a, b, op))