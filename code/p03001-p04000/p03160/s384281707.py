def solve():
    h = read()
    result = think(h)
    write(result)


def read():
    n = read_int(1)[0]
    return read_int(n)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(h):
    cost = [0 for _ in range(len(h))]
    cost[1] = abs(h[1] - h[0])
    for i in range(2, len(h)):
        cost[i] = min(cost[i - 1] + abs(h[i] - h[i - 1]), cost[i - 2] + abs(h[i] - h[i - 2]))
    return cost[len(h) - 1]


def write(result):
    print(result)


if __name__ == '__main__':
    solve()