# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
import copy
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


@mt
def slv(S, T):

    si = defaultdict(deque)
    for i, s in enumerate(S):
        si[s].append(i)

    for k in si:
        si[k].append(-1)

    wsi = si
    used = defaultdict(deque)
    ans = 0
    i = -1
    # from pprint import pprint
    # pprint(si)
    for t in T:
        if t not in wsi:
            return -1

        while wsi[t][0] != -1:
            j = wsi[t].popleft()
            used[t].append(j)
            if j > i:
                i = j
                break
        else:
            ans += len(S)
            for k, q in used.items():
                while q:
                    wsi[k].appendleft(q.pop())
            i = wsi[t].popleft()
            used = defaultdict(deque)
            used[t].append(i)
    return ans + i + 1

def f(S, T):
    ans = -1
    ss = S * 1000
    for t in T:
        if t not in S:
            return -1
        for i in range(ans+1, len(ss)):
            if t == ss[i]:
                ans = i
                break
    return ans + 1





def main():
    S = read_str()
    T = read_str()
    print(slv(S, T))

    # S = ''.join(random.choices('ab', k=3))
    # T = ''.join(random.choices('ab', k=10))
    # print(S)
    # print(T)
    # print(slv(S, T))
    # print(f(S, T))


if __name__ == '__main__':
    main()
