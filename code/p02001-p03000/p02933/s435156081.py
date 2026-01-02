def solve():
    a, s = read()
    result = think(a, s)
    write(result)


def read():
    a = read_int(1)[0]
    s = read_line()
    return a, s


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a, s):
    if a >= 3200:
        return s
    else:
        return 'red'


def write(result):
    print(result)


if __name__ == '__main__':
    solve()