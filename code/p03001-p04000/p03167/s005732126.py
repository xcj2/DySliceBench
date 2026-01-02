import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    mod = 10**9 + 7
    H, W = geta(int)
    g = []
    for _ in range(H):
        g.append(gete())

    dp = [[0] * W for _ in range(H)]

    for i in range(W):
        if g[0][i] == "#": break
        dp[0][i] = 1

    for i in range(H):
        if g[i][0] == "#": break
        dp[i][0] = 1

    for i, gi in enumerate(g[1:], 1):
        for j, gij in enumerate(gi[1:], 1):
            if gij == "#":
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod

    print(dp[H - 1][W - 1])


if __name__ == "__main__":
    main()