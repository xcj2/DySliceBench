def solve():
    data = read();
    result = think(data)
    write(result)


def read():
    return read_line()


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
    if data == 'Sunny':
        return 'Cloudy'
    if data == 'Cloudy':
        return 'Rainy'
    if data == 'Rainy':
        return 'Sunny'


def write(result):
    print(result)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    # import sys
    # sys.setrecursionlimit(10000)
    solve()
