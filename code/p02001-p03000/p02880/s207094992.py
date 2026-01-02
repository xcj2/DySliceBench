def solve():
    n = read()
    result = think(n)
    write(result)


def read():
    return read_int(1)[0]


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(n):
    floor = 1
    ceil = 10
    for x in range(floor, ceil):
        if n % x == 0:
            if n // x in range(floor, ceil):
                return 'Yes'
    return 'No'


def write(result):
    print(result)


if __name__ == '__main__':
    solve()