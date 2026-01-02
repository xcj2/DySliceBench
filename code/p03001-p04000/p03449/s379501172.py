def solve():
    a = read()
    result = think(a)
    write(result)


def read():
    n = read_int(1)[0]
    a = []
    for i in range(2):
        a.append(read_int(n))
    return a


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a):
    x_range = len(a[0])
    y_range = len(a)
    subtotal = [[0 for x in range(x_range)] for y in range(y_range)]
    for y in range(y_range):
        for x in range(x_range):
            if y == 0:
                if x == 0:
                    subtotal[y][x] = a[y][x]
                else:
                    subtotal[y][x] = a[y][x] + subtotal[y][x - 1]
            else:
                if x == 0:
                    subtotal[y][x] = a[y][x] + subtotal[y - 1][x]
                else:
                    subtotal[y][x] = a[y][x] + max(subtotal[y][x - 1], subtotal[y - 1][x])
    return subtotal[y_range - 1][x_range - 1]


def write(result):
    print(result)


if __name__ == '__main__':
    solve()