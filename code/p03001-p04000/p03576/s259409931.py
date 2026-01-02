# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub, itemgetter, attrgetter


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


def ref(N, M, XY):
    ans = INF
    for i in combinations(range(N), r=M):
        minx = INF
        miny = INF
        maxx = -INF
        maxy = -INF
        for j in i:
            x, y = XY[j]
            minx = min(minx, x)
            maxx = max(maxx, x)
            miny = min(miny, y)
            maxy = max(maxy, y)
        ans = min(ans, (maxx-minx)*(maxy-miny))
    return ans

@mt
def slv(N, M, XY):
    XY.sort(key=itemgetter(1))
    XY.sort()
    # print(XY)

    ans = INF
    for i, (x, y) in enumerate(XY):
        yl = [y]
        for j in range(i+1, N):
            x2, y2 = XY[j]
            lx = x2-x
            yl.append(y2)

            if len(yl) >= M:
                yl.sort()
                for k in range(len(yl)-M+1):
                    ly = yl[k+M-1] -  yl[k]
                    ans = min(ans, lx*ly)
    return ans

def main():
    N, M = read_int_n()
    XY = [read_int_n() for _ in range(N)]
    print(slv(N, M, XY))



if __name__ == '__main__':
    main()
