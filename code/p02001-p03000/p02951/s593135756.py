def solve():
    a, b, c = read()
    result = think(a, b, c)
    write(result)


def read():
    return read_int(3)


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
    if b + c >= a:
        return b + c - a
    else:
        return 0


def write(result):
    print(result)


if __name__ == '__main__':
    solve()