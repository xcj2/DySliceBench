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
    from bisect import bisect, bisect_left, bisect_right

    def __init__(self):
        pass

    # aにxが存在するか
    @staticmethod
    def exist(a, x):
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return True
        return False

    # xのindex(なければ-1)
    @staticmethod
    def index(a, x):
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        return -1

    # y < xのようなyの中でもっとも右のindex
    @staticmethod
    def index_lt(a, x):
        i = bisect_left(a, x)
        if i:
            return i - 1
        return -1

    # y < xのようなyの個数
    @staticmethod
    def num_lt(a, x):
        return bisect_left(a, x)

    # y <= xのようなyの中でもっとも右のindex
    @staticmethod
    def index_lte(a, x):
        i = bisect_right(a, x)
        if i:
            return i - 1
        return -1

    # y < xのようなyの個数
    @staticmethod
    def num_lte(a, x):
        return bisect_right(a, x)

    # y > xのようなyの中でもっとも左のindex
    @staticmethod
    def index_gt(a, x):
        i = bisect_right(a, x)
        if i != len(a):
            return i
        return -1

    # y > xのようなyの個数
    @staticmethod
    def num_gt(a, x):
        return len(a) - bisect_right(a, x)

    # y >= xのようなyの中でもっとも左のindex
    @staticmethod
    def index_gte(a, x):
        i = bisect_left(a, x)
        if i != len(a):
            return i
        return -1

    # y >= xのようなyの個数
    @staticmethod
    def num_gte(a, x):
        return len(a) - bisect_left(a, x)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if len(set(A)) != N or len(set(B)) != M:
        print(0)
        return

    MOD = 10 ** 9 + 7

    sorted_A = list(sorted(A[:]))
    sorted_B = list(sorted(B[:]))
    sorted_total = list(sorted(set(A[:] + B[:])))

    ans = 1
    free = 0
    for d in range(N * M, 0, -1):
        in_a = BisectWrapper.exist(sorted_A, d)
        in_b = BisectWrapper.exist(sorted_B, d)
        if in_a and in_b:
            pass
        elif in_a:
            num_b = BisectWrapper.num_gt(sorted_B, d)

            ans *= num_b
            ans %= MOD
        elif in_b:
            num_a = BisectWrapper.num_gt(sorted_A, d)

            ans *= num_a
            ans %= MOD
        else:
            num_a = BisectWrapper.num_gt(sorted_A, d)
            num_b = BisectWrapper.num_gt(sorted_B, d)
            num_t = BisectWrapper.num_gt(sorted_total, d)

            num = num_a * num_b - num_t
            ans *= (num - free)
            ans %= MOD
            free += 1

    print(ans % MOD)


if __name__ == '__main__':
    main()
