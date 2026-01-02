def solve():
    h, k = read()
    result = think(h, k)
    write(result)


def read():
    n, k = read_int(2)
    return read_int(n), k


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(h, k):
    cost = [0 for x in range(len(h))]
    for dst in range(1, len(h)):
        start_point = max(0, dst - k)
        cost[dst] = min([cost[src] + abs(h[src] - h[dst]) for src in range(start_point, dst)])
    return cost[len(h) - 1]


def write(result):
    print(result)


if __name__ == '__main__':
    solve()