def solve():
    k, a = read()
    result = think(k, a)
    write(result)


def read():
    n, k = read_int(2)
    return k, read_int(n)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(k, a):
    mode = 10 ** 9 + 7
    n = len(a)

    # dp[i][j], means ways to count, for from 0th to ith child, candies num is j
    # dp[i][j] = sum(dp[i - 1][j - k]), which k is 0 to a[i]
    dp = [[0 for x in range(k + 1)] for y in range(n)]
    dp[0][0] = 1

    accumulated_a = [0 for x in range(n)]
    accumulated_a[0] = a[0]
    for i in range(1, n):
        accumulated_a[i] = accumulated_a[i - 1] + a[i]

    if accumulated_a[n - 1] < k:
        return 0

    accumulated_dp = [0] * (k + 2)

    # accum[0] = 0
    # accum[1] = dp[i][0]
    # accum[2] = dp[i][0] + dp[i][1]
    # accum[k] = dp[i][0] + dp[i][1] + ... + dp[i][k - 1]
    # accum[k + 1] = dp[i][0] + dp[i][1] + ... + dp[i][k]

    for i in range(n):
        for j in range(min(accumulated_a[i] + 1, k + 1)):
            if i == 0 and j == 0:
                continue
            if i == 0:
                if j <= a[i]:
                    dp[i][j] = 1
            else:
                # add (dp[i - 1][j - a[i]] to dp[i - 1][a[i]])
                dp[i][j] += accumulated_dp[j + 1] - accumulated_dp[max(j - a[i], 0)]
                dp[i][j] %= mode

        for y in range(k + 1):
            accumulated_dp[y + 1] = accumulated_dp[y] + dp[i][y]

    return dp[n - 1][k]


def write(result):
    print(result)


if __name__ == '__main__':
    solve()