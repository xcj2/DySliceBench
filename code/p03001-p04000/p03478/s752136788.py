def solve():
    n, a, b = read()
    result = think(n, a, b)
    write(result)


def read():
    return read_int(3)


def read_int(n):
    return list(map(int, read_line().split()[:n]))


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(n, a, b):
    subsum = 0
    for i in range(1, n + 1):
        if satisfies_condition(i, a, b):
            subsum += i
    return subsum


def satisfies_condition(i, a, b):
    return a <= sum(map(int, list(str(i)))) <= b


def write(result):
    print(result)


if __name__ == '__main__':
    solve()