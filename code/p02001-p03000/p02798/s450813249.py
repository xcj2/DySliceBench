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

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

@mt
def slv(N, A, B):
    AB = list(zip(A, B))


    ans = INF
    for f in product(range(2), repeat=N):
        o = []
        e = []
        for i, (c, ab) in enumerate(zip(f, AB)):
            v = ab[c]
            if i % 2 == 0:
                if c == 0:
                    e.append((v, i))
                else:
                    o.append((v, i))
            else:
                if f[i] == 0:
                    o.append((v, i))
                else:
                    e.append((v, i))
        if 0 <= len(e) - len(o) <= 1:
            bit = Bit(50)
            e.sort()
            o.sort()
            eo = [e, o]
            cand = 0
            p = -1
            for i in range(N):
                if p > eo[i%2][i//2][0]:
                    break
                p = eo[i % 2][i//2][0]
                bit.add(eo[i%2][i//2][1]+1, 1)
                cand += i + 1 - bit.sum(eo[i%2][i//2][1]+1)
            else:
                ans = min(ans, cand)
    if ans == INF:
        ans = -1
    return ans


def main():
    N = read_int()
    A = read_int_n()
    B = read_int_n()
    print(slv(N, A, B))

if __name__ == '__main__':
    main()
