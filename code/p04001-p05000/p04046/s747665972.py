
# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from pprint import pprint
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


nCr = {}


def C(n, r):
    if r == 0 or r == n:
        return 1
    if r == 1:
        return n
    if (n, r) in nCr:
        return nCr[(n, r)]
    nCr[(n, r)] = C(n-1, r) + C(n-1, r-1)
    return nCr[(n, r)]


MOD = 10**9+7  # 出力の制限
N = 10**6
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % MOD)
    inverse.append((-inverse[MOD % i] * (MOD//i)) % MOD)
    g2.append((g2[-1] * inverse[-1]) % MOD)


def cmb(n, r):
    if (r < 0 or r > n):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % MOD


@mt
def slv(H, W, A, B):
    MOD = 10**9+7
    ans = 0
    for i in range(W-B):
        # print(ans)
        w1 = cmb(i+(A-1), i)
        w2 = cmb((W-i-1)+(H-A-1), (H-A-1))
        ans += w1*w2
        ans %= MOD

    return ans % MOD


def main():
    H, W, A, B = read_int_n()

    print(slv(H, W, A, B))


if __name__ == '__main__':
    main()
