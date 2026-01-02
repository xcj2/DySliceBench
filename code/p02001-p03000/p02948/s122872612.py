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
input = sys.stdin.readline


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


# @mt
# def slv(N, M, AB):
#     @lru_cache(maxsize=None)
#     def f(done, day):
#         print(day)
#         if day == M:
#             b = 0
#             for i, d in enumerate(done):
#                 if d == '0':
#                     continue
#                 b += AB[i][1]
#             return b
        
#         ans = 0
#         d_ = [d for d in done]
#         for i, d in enumerate(done):
#             if d == 1 or M - day < AB[i][0]:
#                 continue
#             d_[i] = '1'
#             ans = max(ans, f(''.join(d_), day+1))
#             d_[i] = '0'
#         ans = max(ans, f(''.join(d_), day+1))
#         return ans
#     return f('0'*N, 0)


@mt
def slv(N, M, AB):
    ans = 0
    cand = []
    AB.sort(key=lambda x: x[0], reverse=True)
    for i in range(1, M+1):
        while AB and AB[-1][0] <= i:
            a, b = AB.pop()
            heapq.heappush(cand, -b)
        if cand:
            ans -= heapq.heappop(cand)
    return ans 

def main():
    N, M = read_int_n()
    AB = [read_int_n() for _ in range(N)]
    print(slv(N, M, AB))

    # N = 10**5
    # M = 10**5
    # AB = [[random.randint(1, 10**5), random.randint(1, 10**4)] for _ in range(N)]
    # print(slv(N, M, AB))


if __name__ == '__main__':
    main()
