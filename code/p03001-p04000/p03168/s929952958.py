import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    N = gete(int)
    # p = tuple(geta(lambda s: int(s.decode()[2:])))
    p = tuple(geta(float))

    dp = [[0] * (i + 2) for i in range(N + 1)]
    dp[0][0] = 1

    for i, pi in enumerate(p, 1):
        qi = 1 - pi
        dpi = dp[i]
        dpi1 = dp[i - 1]

        dpi[0] = dpi1[0] * qi

        for j in range(1, i + 1):
            dpi[j] = dpi1[j - 1] * pi + dpi1[j] * qi

    print(sum(dp[N][N // 2 + 1:]))


if __name__ == "__main__":
    main()