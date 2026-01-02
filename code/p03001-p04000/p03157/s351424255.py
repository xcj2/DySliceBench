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

sys.setrecursionlimit(10000)


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
def slv(H, W, S):
    g = defaultdict(dict)
    for i, r in enumerate(S):
        for j, c in enumerate(r):
            if i > 0 and S[i-1][j] != c:
                g[(i, j)][(i-1, j)] = 1
                g[(i-1, j)][(i, j)] = 1
            if i < H-1 and S[i+1][j] != c:
                g[(i, j)][(i+1, j)] = 1
                g[(i+1, j)][(i, j)] = 1
            if j > 0 and S[i][j-1] != c:
                g[(i, j)][(i, j-1)] = 1
                g[(i, j-1)][(i, j)] = 1
            if j < W-1 and S[i][j+1] != c:
                g[(i, j)][(i, j+1)] = 1
                g[(i, j+1)][(i, j)] = 1
    
    done = set([])
    ans = 0
    ac = {}
    for k in g:
        
        i, j = k
        if S[i][j] != '#':
            continue
        
        if k in ac:
            ans += ac[k]
            continue
        s = [k]
        done = set([k])
        w = set([])
        count = 0
        while s:
            # print(s)
            k = s.pop()
            for n in g[k]:
                if n not in done:
                    s.append(n)
                    done.add(n)
            i, j = k
            if S[i][j] == '.':
                count += 1
            else:
                w.add(k)
        for l in w:
            ac[l] = count
        ans += count
        

    return ans


def main():
    H, W = read_int_n()
    S = []
    for _ in range(H):
        S.append(read_str())
    # S = []
    # H = 400
    # W = 400
    # for i in range(H):
    #     if i%2 == 0:
    #         S.append('#.'*200)
    #     else:
    #         S.append('.#'*200)

    print(slv(H, W, S))


if __name__ == '__main__':
    main()
