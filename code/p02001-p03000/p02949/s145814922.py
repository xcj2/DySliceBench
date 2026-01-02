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


def BellmanFord(N, e, s, goal):
    dist = [sys.maxsize] * (N+1)
    dist[s] = 0
    for i in range(N+1):
        for u, v, c in e:
            if dist[v] > dist[u] + c:
                if i == N:
                    return 'inf'
                dist[v] = dist[u] + c
    return dist

@mt
def slv(N, M, P, ABC):
    g = [[] for _ in range(N+1)]
    for a, b, c in ABC:
        g[a].append(b)

    def r(s, e):
        q = deque()
        q.append(s)
        done = set([s])
        while q:
            u = q.pop()
            for v in g[u]:
                if v not in done:
                    done.add(v)
                    q.append(v)
        return done

    d = set()
    for i in range(2, N):
        reachable = r(i, N)
        if N not in reachable:
            d.add(i)
    
    e = []
    sr = r(1, N)
    for a, b, c in ABC:
        if a not in d and b not in d and a in sr and b in sr:
            e.append((a, b, -(c - P)))

    d = BellmanFord(N, e, 1, N)
    if d == 'inf':
        return -1
    return max(0, -d[N])


def main():
    N, M, P = read_int_n()
    ABC = [read_int_n() for _ in range(M)]
    print(slv(N, M, P, ABC))

    # N = 2500
    # M = 5000
    # P = random.randint(0, 10**5)
    # P= 0
    # ABC = [
    #     [random.randint(1, N), random.randint(1, N), random.randint(1, 10**5)] for _ in range(M)
    # ]
    # print(slv(N, M, P, ABC))



if __name__ == '__main__':
    main()
