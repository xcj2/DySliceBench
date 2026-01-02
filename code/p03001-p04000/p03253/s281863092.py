# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub

sys.setrecursionlimit(10000)


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input().strip()


def read_str_n():
    return list(map(str, input().split()))


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap


class Combination:
    def __init__(self, n, mod):

        g1 = [1, 1]
        g2 = [1, 1]
        inverse = [0, 1]
        for i in range(2, n + 1):
            g1.append((g1[-1] * i) % mod)
            inverse.append((-inverse[mod % i] * (mod//i)) % mod)
            g2.append((g2[-1] * inverse[-1]) % mod)
        self.MOD = mod
        self.N = n
        self.g1 = g1
        self.g2 = g2
        self.inverse = inverse

    def __call__(self, n, r):
        if (r < 0 or r > n):
            return 0
        r = min(r, n-r)
        return self.g1[n] * self.g2[r] * self.g2[n-r] % self.MOD


def fs(n):
    f = Counter()
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        error_print(i)
        if i > n:
            break
        while n % i == 0:
            f[i] += 1
            n /= i
    if n != 1:
        f[n] = 1
    return f


mod = 10**9 + 7


def mod_mul(a, b):
    return ((a % mod) * (b % mod)) % mod


def mod_power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x % mod
    elif y % 2 == 0:
        return mod_power(x, y/2)**2 % mod
    else:
        return mod_power(x, y/2)**2 * x % mod


def mod_div(a, b):
    return mod_mul(a, mod_power(b, mod-2))


def P(n):
    ans = 1
    for i in range(2, n+1):
        ans = mod_mul(ans, i)

    return ans


@mt
def slv(N, M):
    f = fs(M)
    ans = 1
    error_print(f)
    C = Combination(10**6, mod)

    for k in f:
        ans = mod_mul(ans, C(N+f[k]-1, f[k]) % mod)
    return ans


def main():
    N, M = read_int_n()
    print(slv(N, M))


if __name__ == '__main__':
    main()
