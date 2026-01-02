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
    n = int(input())
    V = list(map(int, input().split()))

    d1, d2 = defaultdict(int), defaultdict(int)
    for i in range(n):
        if i % 2 == 0:
            d1[V[i]] += 1
        else:
            d2[V[i]] += 1

    if len(set(V)) == 1:
        print(n // 2)
        return

    num = n // 2
    ans = INF
    for k1, v1 in sorted(d1.items(), key=lambda x:x[1], reverse=True)[:2]:
        for k2, v2 in sorted(d2.items(), key=lambda x:x[1], reverse=True)[:2]:
            if k1 != k2:
                t = (num - v1) + (num - v2)
                ans = min(ans, t)

    print(ans)


if __name__ == '__main__':
    main()
