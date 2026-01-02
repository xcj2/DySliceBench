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


def exist(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    return False


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
        in_a = exist(sorted_A, d)
        in_b = exist(sorted_B, d)
        if in_a and in_b:
            pass
        elif in_a:
            num_b = (M - bisect_left(sorted_B, d))

            ans *= num_b
            ans %= MOD
        elif in_b:
            num_a = (N - bisect_left(sorted_A, d))

            ans *= num_a
            ans %= MOD
        else:
            num_a = (N - bisect_left(sorted_A, d))
            num_b = (M - bisect_left(sorted_B, d))
            num_t = (len(sorted_total) - bisect_left(sorted_total, d))

            num = num_a * num_b - num_t
            ans *= (num - free)
            ans %= MOD
            free += 1

    print(ans % MOD)


if __name__ == '__main__':
    main()
