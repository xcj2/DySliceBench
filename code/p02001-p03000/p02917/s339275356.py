def solve():
    data = read()
    result = think(data)
    write(result)


def read():
    n = read_int(1)[0]
    return read_int(n - 1)


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
    result = []
    result.append(data[0])
    for i in range(len(data) - 1):
        result.append(min(data[i], data[i + 1]))
    result.append(data[-1])
    return sum(result)


def write(result):
    print(result)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    # import sys
    # sys.setrecursionlimit(10000)
    solve()