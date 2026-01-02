import sys


def solve():
    a = read()
    result = think(a)
    write(result)


def read():
    h, w = read_int(2)
    a = []
    for y in range(h):
        a.append(read_line(n=w))
    return a


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a):
    mode = 10 ** 9 + 7
    wall_symbol = '#'

    h = len(a)
    w = len(a[0])

    ways_count_to_get = [[0 for x in range(w)] for y in range(h)]
    ways_count_to_get[0][0] = 1

    for y in range(h):
        for x in range(w):
            if x == 0 and y == 0:
                continue
            if x == 0:
                if a[y][x] == wall_symbol:
                    continue
                else:
                    ways_count_to_get[y][x] = ways_count_to_get[y - 1][x]
                    continue
            if y == 0:
                if a[y][x] == wall_symbol:
                    continue
                else:
                    ways_count_to_get[y][x] = ways_count_to_get[y][x - 1]
                    continue
            if a[y][x] == wall_symbol:
                ways_count_to_get[y][x] = 0
            else:
                ways_count_to_get[y][x] = (ways_count_to_get[y - 1][x] + ways_count_to_get[y][x - 1]) % mode

    return ways_count_to_get[h - 1][w - 1]


def write(result):
    print(result)


if __name__ == '__main__':
    sys.setrecursionlimit(1000 * 1000)
    solve()