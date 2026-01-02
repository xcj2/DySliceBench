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
INF = 2**62-1

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


def dc(n, m):
    return -(-n // m)

# @mt
def slv(H, N, AB):
    ans = 0
    abc = [(a/b, b, a) for a, b in AB]

    abc.sort(key=lambda x: x[1])
    abc.sort(key=lambda x: x[2])
    abc.sort(key=lambda x: x[0], reverse=True)
    # ri = set()
    # mm = INF
    # for i in range(N):
    #     if abc[i][1] >= mm:
    #         ri.add(i)
    #     else:
    #         mm = abc[i][1]
    # ri = set(ri)
    # abc_ = []
    # for i in range(N):
    #     if i not in ri:
    #         abc_.append(abc[i])
    # error_print(abc)
    # abc = abc_
    # error_print(abc)

    HD = defaultdict(lambda : INF)
    HD[H] = 0
    _, b, a = abc[0]
    for i in range(1, dc(H, a)+1):
        HD[H - i*a] = i*b
    for _, b, a in abc[1:]:
        for k, v in reversed(list(HD.items())):
            for i in range(1, dc(k, a)+1):
                if HD[k - i*a] > v+i*b:
                    HD[k- i*a] = v+i*b
                else:
                    break
    ans = INF
    for k, v in HD.items():
        if k <= 0:
            ans = min(ans, v)


    return ans


def main():
    H, N = read_int_n()
    AB = [read_int_n() for _ in range(N)]
    print(slv(H, N, AB))
    # H = 10**4
    # N = 10
    # AB = [[random.randint(1, 100), random.randint(1, 100)] for _ in range(N)]
    # print(slv(H, N, AB))


if __name__ == '__main__':
    main()
