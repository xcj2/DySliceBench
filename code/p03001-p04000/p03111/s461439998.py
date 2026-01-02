from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
import sys
sys.setrecursionlimit(100000)
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


def dfs(i, a, b, c, N, A, B, C, L):
    if i >= N:
        if a == 0 or b == 0 or c == 0:
            return INF
        return abs(A - a) + abs(B - b) + abs(C - c)

    ret = INF
    ret = min(ret, dfs(i + 1, a + L[i], b, c, N, A, B, C, L) + (10 if a > 0 else 0))
    ret = min(ret, dfs(i + 1, a, b + L[i], c, N, A, B, C, L) + (10 if b > 0 else 0))
    ret = min(ret, dfs(i + 1, a, b, c + L[i], N, A, B, C, L) + (10 if c > 0 else 0))
    ret = min(ret, dfs(i + 1, a, b, c, N, A, B, C, L))

    return ret


def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]

    print(dfs(0, 0, 0, 0, N, A, B, C, L))


if __name__ == '__main__':
    main()
