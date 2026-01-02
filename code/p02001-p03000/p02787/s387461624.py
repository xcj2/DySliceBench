import sys
from collections import defaultdict

readline = sys.stdin.buffer.readline


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


sys.setrecursionlimit(10**5)


def main():
    h, n = geta(int)
    a, b = [0] * (n + 1), [0] * (n + 1)
    for i in range(n):
        a[i + 1], b[i + 1] = geta(int)

    INF = 10**9
    dp = [[INF] * (h + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(0, h + 1):
            if j <= a[i]:
                dp[i][j] = min(b[i], dp[i - 1][j])
            else:
                dp[i][j] = min(dp[i][j - a[i]] + b[i], dp[i - 1][j])

    print(dp[n][h])


if __name__ == "__main__":
    main()