def solve():
    a, b, c, d = read()
    result = think(a, b, c, d)
    write(result)


def read():
    return read_int(4)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a, b, c, d):
    if b <= c or d <= a:
        return 0
    elif a <= c and d <= b:
        return d - c
    elif c <= a and b <= d:
        return b - a
    else:
        if a == c:
            return min(b, d) - a
        elif a < c:
            return abs(c - b)
        else:  # a > c
            return abs(d - a)


def write(result):
    print(result)


if __name__ == '__main__':
    solve()