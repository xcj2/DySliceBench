import sys
# import re
import math
import collections
# import decimal
import bisect
import itertools
import fractions
# import functools
import copy
# import heapq
import decimal
# import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===
def fast_pow(num, kata, mod):
    if kata == 0:
        return 1

    res = 1
    while kata > 0:
        if kata & 1 == 1:
            res = res * num % mod
        num = num * num % mod

        kata >>= 1
    return res


def choose(n, r, MOD):
    res = 1
    fac = 1
    for i in range(r):
        res *= n - i
        res %= MOD
        fac *= i + 1
        fac %= MOD
    return res * fast_pow(fac, MOD - 2, MOD) % MOD


# nCrの左項にはn以外も来るバージョン、1!～(n-1)!を保持
def prepare(n, MOD):
    # 1! - n! の計算
    f = 1
    factorials = [1]  # 0!の分
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    # n!^-1 の計算
    inv = pow(f, MOD - 2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv

    return factorials, invs


def main():
    k = ni()
    s = input()
    l = len(s)

    # 使い方
    facts, invs = prepare(k + l, MOD)

    ans = 0
    for ki in range(k + 1):
        tmpa = fast_pow(25, k - ki, MOD)
        tmpb = fast_pow(26, ki, MOD)
        tmpc = facts[k - ki + l - 1] * invs[l - 1] * invs[k - ki + l - 1 - (l - 1)] % MOD
        tmpd = (tmpa * tmpb * tmpc) % MOD
        ans += tmpd
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()
