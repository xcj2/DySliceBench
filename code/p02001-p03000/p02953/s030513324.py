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
    n = len(h)
    invalid = 10 ** 20

    dp = [[0 for x in range(2)] for y in range(len(h))]
    dp[0][0] = h[0]
    dp[0][1] = h[0] - 1
    for i in range(1, len(h)):
        dp[i][0] = h[i]
        dp[i][1] = h[i] - 1

        if dp[i][0] < dp[i - 1][0] and dp[i][0] < dp[i - 1][1]:
            dp[i][0] = invalid
        elif dp[i][0] < dp[i - 1][0] and dp[i][0] >= dp[i - 1][1]:
            dp[i][0] = h[i]
        elif dp[i][0] >= dp[i - 1][0] and dp[i][0] >= dp[i - 1][1]:
            dp[i][0] = h[i]
        elif dp[i][0] >= dp[i - 1][0] and dp[i][0] < dp[i - 1][1]:
            dp[i][0] = h[i]

        if dp[i][1] < dp[i - 1][0] and dp[i][1] < dp[i - 1][1]:
            dp[i][1] = invalid
        elif dp[i][1] < dp[i - 1][0] and dp[i][1] >= dp[i - 1][1]:
            dp[i][1] = h[i] - 1
        elif dp[i][1] >= dp[i - 1][0] and dp[i][1] >= dp[i - 1][1]:
            dp[i][1] = h[i] - 1
        elif dp[i][1] >= dp[i - 1][0] and dp[i][1] < dp[i - 1][1]:
            dp[i][1] = h[i] - 1

    return dp[n - 1][0] < invalid or dp[n - 1][1] < invalid


def write(result):
    if result:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()