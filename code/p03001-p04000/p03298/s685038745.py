# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul

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
    return list(map(str, input().strip().split()))


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


def ref_slv(N, S):
    ans = 0

    for i in combinations(range(0, 2*N), N):
        l = []
        r = []
        for j in range(2*N):
            if j in i:
                l.append(S[j])
            else:
                r.append(S[j])

        if ''.join(l) == ''.join(reversed(r)):
            ans += 1

    return ans


@mt
def slv(N, S):
    ans = 0

    l = S[:N]
    r = S[N:][::-1]
    ld = defaultdict(lambda: 0)
    rd = defaultdict(lambda: 0)

    for i in range(N+1):
        for j in combinations(range(N), i):
            lb = []
            lr = []
            rb = []
            rr = []
            for k in range(N):
                if k in j:
                    lb.append(l[k])
                    rr.append(r[k])
                else:
                    lr.append(l[k])
                    rb.append(r[k])
            ld[(''.join(lr), ''.join(lb))] += 1
            rd[(''.join(rr), ''.join(rb))] += 1
    for k, v in ld.items():
        if k in rd:
            ans += v * rd[k]

    return ans


def main():
    # for i in range(1, 19):
    #     print(i, slv(i, ""))
    N = read_int()
    S = read_str()
    print(slv(N, S))


if __name__ == '__main__':
    main()
