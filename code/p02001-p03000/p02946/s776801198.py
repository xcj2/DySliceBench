def solve():
    k, x = read()
    result = think(k, x)
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


def think(k, x):
    minimum = -1000000
    maximum = 1000000

    left = max(x - k + 1, minimum)
    right = min(x + k - 1, maximum)

    return list(range(left, right + 1))


def write(result):
    print(' '.join(map(str, result)))


if __name__ == '__main__':
    solve()