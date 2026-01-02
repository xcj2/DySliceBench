from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
INF = float("inf")
YES, Yes, yes, NO, No, no = "YES", "Yes", "yes", "NO", "No", "no"
dy4, dx4 = [0, 1, 0, -1], [1, 0, -1, 0]
dy8, dx8 = [0, -1, 0, 1, 1, -1, -1, 1], [1, 0, -1, 0, 1, 1, -1, -1]


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def ceil(a, b):
    return (a + b - 1) // b


# aとbの最大公約数
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# aとbの最小公倍数
def lcm(a, b):
    g = gcd(a, b)
    return a / g * b


def main():
    H, W, K = map(int, input().split())
    MOD = 10 ** 9 + 7

    num = [[0] * 9 for _ in range(9)]
    for b in range(2 ** (W - 1)):
        b = bin(b)[2:].zfill(W - 1)
        ok = True
        for i in range(len(b) - 1):
            if b[i] == "1" and b[i + 1] == "1":
                ok = False
        if ok:
            p = list(range(W))
            for i in range(len(b)):
                if b[i] == "1":
                    p[i], p[i + 1] = p[i + 1], p[i]

            for i in range(W):
                num[i][p[i]] += 1

    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[0][0] = 1
    for y in range(H):
        for x in range(W):
            for i in range(W):
                dp[y + 1][i] += dp[y][x] * num[x][i]
                dp[y + 1][i] %= MOD

    print(dp[H][K - 1])


if __name__ == '__main__':
    main()
