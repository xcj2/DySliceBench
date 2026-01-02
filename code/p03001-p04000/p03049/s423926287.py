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

sys.setrecursionlimit(100000)


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


@mt
def slv(N, S):
    ans = 0
    pre_b = set()
    post_a = set()
    for i, s in enumerate(S):
        if s[0] == 'B':
            pre_b.add(i)
        if s[-1] == 'A':
            post_a.add(i)
        ans += s.count('AB')
    # error_print(ans)
    both = pre_b & post_a
    if both:
        ans += len(pre_b & post_a) - 1
    pre_b -= both
    post_a -= both
    # print(pre_b, post_a)
    pbl = len(pre_b)
    pal = len(post_a)
    if both:
        if pbl == 0 and pal == 0:
            pass
        elif pbl == 0:
            # print(min(max(pbl, 1), max(pal, 1),))
            ans += min(1, pal)
        elif pal == 0:
            ans += min(1, pbl)
        else:
            ans += min(pbl+1, pal+1)
    else:
        ans += min(pbl, pal)
    return ans


def slv2(N, S):
    ans = 0
    for i in permutations(range(N), N):
        ans = max(ans, ''.join([S[j] for j in i]).count('AB'))
    return ans


def main():
    N = read_int()
    S = [read_str() for _ in range(N)]
    print(slv(N, S))
    # print(slv2(N, S))

    # for _ in range(1000):
    #     N = 5
    #     S = [''.join(random.choices('ABC', k=5)) for _ in range(N)]
    #     if slv2(N, S) != slv(N, S):
    #         print(S)
    #         break


if __name__ == '__main__':
    main()
