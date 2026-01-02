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
    if b == 1:
        return 0
    accum = [a + (a - 1) * r for r in range(100)]
    for i in range(len(accum)):
        if accum[i] >= b:
            return i + 1


def write(result):
    print(result)

if __name__ == '__main__':
    solve()