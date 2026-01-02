def reverse_polish_calculator(s):
    """Calculate a reverse polish notation s.
    + - * operators can be used in s. Only positive integer is
    supported for operand.

    >>> reverse_polish_calculator("1 2 +")
    3
    >>> reverse_polish_calculator("1 2 + 3 4 - *")
    -3
    """
    def calc(val1, op, val2):
        if op == '+':
            return val1 + val2
        elif op == '-':
            return val1 - val2
        elif op == '*':
            return val1 * val2
        else:
            raise ValueError()

    stack = []
    for c in s.split():
        if c.isnumeric():
            stack.append(int(c))
        else:
            v2 = stack.pop()
            v1 = stack.pop()
            stack.append(calc(v1, c, v2))

    return stack.pop()


def run():
    s = input()
    print(reverse_polish_calculator(s))


if __name__ == '__main__':
    run()
