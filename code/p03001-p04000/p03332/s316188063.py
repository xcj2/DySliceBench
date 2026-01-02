# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product

sys.setrecursionlimit(10000)

MOD = 998244353


def mul_mod(a, b):
    return (a % MOD) * (b % MOD) % MOD


def add_mod(a, b):
    return (a + b) % MOD


def sub_mod(a, b):
    return (a - b) % MOD


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input()


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


def prepare(n):
    f = 1
    for m in range(1, n + 1):
        f *= m
        f %= MOD
    fn = f
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv

    return fn, invs


@mt
def slv(N, A, B, K):
    ans = 0

    FN, invs = prepare(N)
    for i in range(K // A + 1):
        if (K - i * A) % B == 0 and i <= N and (K - i * A) // B <= N:
            j = (K - i * A) // B
            error_print(i, j)
            ans = add_mod(ans,
                          mul_mod(FN * invs[i] * invs[N - i] % MOD,
                                  FN * invs[j] * invs[N - j] % MOD))

    return ans


def main():
    N, A, B, K = read_int_n()
    print(slv(N, A, B, K))


if __name__ == '__main__':
    main()
