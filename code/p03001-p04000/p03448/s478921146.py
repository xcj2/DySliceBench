def solve():
    a, b, c, x = read()
    result = think(a, b, c, x)
    write(result)


def read():
    a = read_int(1)[0]
    b = read_int(1)[0]
    c = read_int(1)[0]
    x = read_int(1)[0]
    return a, b, c, x


def read_int(n):
    return list(map(int, read_line().split()[:n]))


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a, b, c, x):
    count = 0
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                if 500 * i + 100 * j + 50 * k == x:
                    count += 1
    return count


def write(result):
    print(result)


if __name__ == '__main__':
    solve()