# -*- coding: utf-8 -*-
# import bisect
# import heapq
# import math
# import random
# from collections import Counter, defaultdict, deque
# from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache
# from itertools import combinations, combinations_with_replacement, product, permutations
# from operator import add, mul, sub


import sys
# sys.setrecursionlimit(10**6)
# buff_readline = sys.stdin.buffer.readline
buff_readline = sys.stdin.readline
readline = sys.stdin.readline

INF = 2**62-1


def read_int():
    return int(buff_readline())


def read_int_n():
    return list(map(int, buff_readline().split()))


def read_float():
    return float(buff_readline())


def read_float_n():
    return list(map(float, buff_readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()

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


# @mt
def slv(N, A, B, C, D):
    if N == 1:
        return D

    @lru_cache(maxsize=None)
    def f(n):
        ans = n*D
        for i in range(-5, 6 if n > 10 else 1):
            m = n + i
            i = abs(i)
            if m < 0:
                continue
            if m == 0:
                ans = min(ans, D*i)
                continue

            if m % 5 == 0:
                ans = min(ans, f(m//5) + C + D*i)
                # ans = min(ans, f(m//5) + 4*(m//5)*D + D*i)
            if m % 3 == 0:
                ans = min(ans, f(m//3) + B + D*i)
                # ans = min(ans, f(m//3) + 2*(m//3)*D + D*i)
            if m % 2 == 0:
                ans = min(ans, f(m//2) + A + D*i)
                # ans = min(ans, f(m//2) + (m//2)*D + D*i)
        return ans

    return f(N)


def main():
    T = read_int()
    for _ in range(T):
        N, A, B, C ,D = read_int_n()
        print(slv(N, A, B, C, D))

    # N, A, B, C, D = 29384293847243, 454353412, 332423423, 934923490, 1
    # print(slv(N, A, B, C, D))


if __name__ == '__main__':
    main()
