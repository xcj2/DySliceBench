def solve():
    a, b = read()
    result = think(a, b)
    write(result)


def read():
    return read_int(2)

def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a, b):
    if a < 2 * b:
        return 0
    return a - 2 * b


def write(result):
    print(result)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    # import sys
    # sys.setrecursionlimit(10000)
    solve()
