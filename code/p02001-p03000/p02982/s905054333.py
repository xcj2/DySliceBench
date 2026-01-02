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


# 初項s, 交差dのn個の数列の和
def sum_of_arithmetic_progression(s, d, n):
    return n * (2 * s + (n - 1) * d) // 2


# aとbの最大公約数
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# aとbの最小公倍数
def lcm(a, b):
    g = gcd(a, b)
    return a / g * b


def func(x1, x2):
    r = 0
    for i in range(len(x1)):
        r += (x1[i] - x2[i]) ** 2

    a = int(sqrt(r))
    return a ** 2 == r or (a - 1) ** 2 == r or (a + 1) ** 2 == r


def main():
    N, D = map(int, input().split())

    dot = []
    for _ in range(N):
        x = list(map(int, input().split()))
        dot.append(x)

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += func(dot[i], dot[j])
    print(ans)


if __name__ == '__main__':
    main()
