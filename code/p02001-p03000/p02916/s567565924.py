def solve():
    a, b, c = read()
    result = think(a, b, c)
    write(result)


def read():
    n = read_int(1)[0]
    a = read_int(n)
    b = read_int(n)
    c = read_int(n - 1)
    return a, b, c


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a, b, c):
    satisfaction = 0
    prev = -1
    for e in a:
        satisfaction += b[e - 1]
        if prev == e - 1:
            satisfaction += c[prev - 1]
        prev = e
    return satisfaction


def write(result):
    print(result)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    # import sys
    # sys.setrecursionlimit(10000)
    solve()