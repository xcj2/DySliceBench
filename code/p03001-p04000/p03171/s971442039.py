def solve():
    a = read()
    result = think(a)
    write(result)


def read():
    n = read_int(1)[0]
    return read_int(n)


def read_int(n):
    return list(map(int, read_line().split(' ')))[:n]


def read_float(n):
    return list(map(float, read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a):
    n = len(a)
    dp = [[None for x in range(n)] for y in range(n)]
    for i in range(len(dp)):
        dp[i][i] = a[i]
    for l in range(n - 2, -1, -1):
        for r in range(l + 1, n):
            dp[l][r] = max(a[l] - dp[l + 1][r], a[r] - dp[l][r - 1])
    return dp[0][n - 1]


def write(result):
    print(result)


if __name__ == '__main__':
    solve()