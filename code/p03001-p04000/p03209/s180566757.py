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


def check(N, X):
    s = "P"
    for i in range(N):
        s = "B" + s + "P" + s + "B"
    return s[:X].count("P")


def func(N, X, P, B):
    if X == 0:
        return 0
    if N == 0:
        return 1

    num = P[N - 1] + B[N - 1]

    ans = 0
    X -= 1
    if X >= num:
        ans += P[N - 1]
        X -= num
    else:
        return func(N - 1, X, P, B)

    if X <= 0:
        return ans
    X -= 1
    ans += 1
    if X <= 0:
        return ans

    if X >= num:
        X -= num
        ans += P[N - 1]
    else:
        return ans + func(N - 1, X, P, B)

    X -= 1

    return ans


def solve(N, X):
    P = [0] * 51
    B = [0] * 51
    P[0] = 1
    for i in range(1, 51):
        P[i] = P[i - 1] * 2 + 1
        B[i] = B[i - 1] * 2 + 2

    return func(N, X, P, B)


def main():
    N, X = map(int, input().split())
    print(solve(N, X))


if __name__ == '__main__':
    main()
