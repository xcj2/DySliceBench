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


class BisectWrapper:
    try:
        from typing import List
    except:
        List = list
    from bisect import bisect, bisect_left, bisect_right

    def __init__(self):
        pass

    # aにxが存在するか
    @staticmethod
    def exist(a: List, x: int):
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return True
        return False

    # xのindex(なければ-1)
    @staticmethod
    def index(a: List, x: int):
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        return -1

    # y < xのようなyの中でもっとも右のindex
    @staticmethod
    def index_lt(a: List, x: int):
        i = bisect_left(a, x)
        if i:
            return i - 1
        return -1

    # y < xのようなyの個数
    @staticmethod
    def num_lt(a: List, x: int):
        return bisect_left(a, x)

    # y <= xのようなyの中でもっとも右のindex
    @staticmethod
    def index_lte(a: List, x: int):
        i = bisect_right(a, x)
        if i:
            return i - 1
        return -1

    # y < xのようなyの個数
    @staticmethod
    def num_lte(a: List, x: int):
        return bisect_right(a, x)

    # y > xのようなyの中でもっとも左のindex
    @staticmethod
    def index_gt(a: List, x: int):
        i = bisect_right(a, x)
        if i != len(a):
            return i
        return -1

    # y > xのようなyの個数
    @staticmethod
    def num_gt(a: List, x: int):
        return len(a) - bisect_right(a, x)

    # y >= xのようなyの中でもっとも左のindex
    @staticmethod
    def index_gte(a: List, x: int):
        i = bisect_left(a, x)
        if i != len(a):
            return i
        return -1

    # y >= xのようなyの個数
    @staticmethod
    def num_gte(a: List, x: int):
        return len(a) - bisect_left(a, x)


def near(A, x):
    l = BisectWrapper.index_lte(A, x)
    r = l + 1
    if l == -1:
        return abs(x - A[r])
    if r >= len(A):
        return abs(x - A[l])
    return min(abs(x - A[r]), abs(x - A[l]))


def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]

    for _ in range(Q):
        x = int(input())

        ans = INF
        s_l = BisectWrapper.index_lte(S, x)
        if s_l != -1:
            s = S[s_l]
            ans = min(ans, abs(x - s) + near(T, s))

        s_r = s_l + 1
        if s_r < len(S):
            s = S[s_r]
            ans = min(ans, abs(x - s) + near(T, s))

        t_l = BisectWrapper.index_lte(T, x)
        if t_l != -1:
            t = T[t_l]
            ans = min(ans, abs(x - t) + near(S, t))

        t_r = t_l + 1
        if t_r < len(T):
            t = T[t_r]
            ans = min(ans, abs(x - t) + near(S, t))

        print(ans)


if __name__ == '__main__':
    main()
