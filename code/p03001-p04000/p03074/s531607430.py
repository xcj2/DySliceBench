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
def slv(N, K, S):
    s1 = list(map(lambda x: len(x), filter(lambda x: x != '', S.split('0'))))
    s0 = list(map(lambda x: len(x), filter(lambda x: x != '', S.split('1'))))
    if len(s0) <= K:
        return N

    if S[0] == '0':
        s1.insert(0, 0)
    if S[-1] == '0':
        s1.append(0)

    q = deque()
    q.append(s1.pop())
    q.append(s0.pop())
    q.append(s1.pop())
    tmp = sum(q)
    ans = tmp
    while s1 or s0:
        if len(q) >= 2*K + 1:
            tmp -= q.popleft()
            tmp -= q.popleft()
        q.append(s0.pop())
        tmp += q[-1]
        q.append(s1.pop())
        tmp += q[-1]
        ans = max(ans, tmp)

    return ans


def main():
    N, K = read_int_n()
    S = read_str()
    print(slv(N, K, S))

    # N = 20
    # K = random.randint(1, 10)
    # S = ''.join(random.choices('01', k=N))
    # rS = ''.join(['0' if c == '1' else '1' for c in S])
    # print(max(slv(N, K, S), slv(N, K-1, rS)))

if __name__ == '__main__':
    main()
