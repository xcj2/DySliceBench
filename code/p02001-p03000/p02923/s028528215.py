def solve():
    h = read()
    result = think(h)
    write(result)


def read():
    n = read_int(1)[0]
    return read_int(n)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(h):
    dp = [0 for x in range(len(h))]
    for i in range(len(h) - 2, -1, -1):
        if h[i] >= h[i + 1]:
            dp[i] = dp[i + 1] + 1
        else:
            dp[i] = 0
    return max(dp)


def write(result):
    print(result)


if __name__ == '__main__':
    solve()