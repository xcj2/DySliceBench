# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub


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


@mt
def slv(H, W, C, D, S):

    C = (C[0]-1, C[1]-1)
    D = (D[0]-1, D[1]-1)
    q = deque()
    q.append((0, C))
    memo = {}
    T = 10**6
    while q:
        c, (x, y) = q.popleft()
        if (x*T + y) in memo:
            continue
        memo[x*T + y] = c
        for nx, ny in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
            if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '.':
                q.appendleft((c, (nx, ny)))

        for nx in range(x-2, x+3):
            for ny in range(y-2, y+3):
                if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '.':
                    q.append((c+1, (nx, ny)))

    return -1 if (D[0]*T + D[1]) not in memo else memo[D[0]*T + D[1]]


def main():
    H, W = read_int_n()
    C = read_int_n()
    D = read_int_n()
    S = [read_str() for _ in range(H)]
    print(slv(H, W, C, D, S))


if __name__ == '__main__':
    main()
