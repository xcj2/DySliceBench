def solve():
    data = read()
    result = think(data)
    write(result)


def read():
    n = read_int(1)[0]
    return read_int(n)

def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(data):
    n = len(data)
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            total += data[i] * data[j]
    return total


def write(result):
    print(result)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    # import sys
    # sys.setrecursionlimit(10000)
    solve()
