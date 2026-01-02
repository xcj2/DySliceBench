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

    for i, gi in enumerate(g):
        if i == 0:
            w = gi.index("#") if "#" in gi else W
            dp[0] = [1 if j < w else 0 for j in range(W)]
        else:
            for j, gij in enumerate(gi):
                if gij == "#":
                    dp[i][j] = 0
                else:
                    dp[i][j] = (dp[i - 1][j] +
                                (dp[i][j - 1] if j > 0 else 0)) % mod

    print(dp[H - 1][W - 1])


if __name__ == "__main__":
    main()