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

sys.setrecursionlimit(10**6)
buff_readline = sys.stdin.buffer.readline
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
def slv(N, A, B, C, S):
    D = [A, B, C]
    ans = []

    def f(s):
        t = []
        if 'A' in s:
            t.append(0)
        if 'B' in s:
            t.append(1)
        if 'C' in s:
            t.append(2)
        return t
    for i, s in enumerate(S):
        t = f(s)
        if D[t[0]] == 0 and D[t[1]] == 0:
            print('No')
            return
        else:
            if D[t[0]] == D[t[1]] == 1 and i != N-1:
                ns = S[i+1]
                if s == ns:
                    ans.append(t[1])
                    D[t[0]] -= 1
                    D[t[1]] += 1
                else:
                    n = set(t) & set(f(ns))
                    m = set(t) - n
                    n = n.pop()
                    m = m.pop()
                    ans.append(n)
                    D[n] += 1
                    D[m] -= 1


            elif D[t[0]] > D[t[1]]:
                ans.append(t[1])
                D[t[0]] -= 1
                D[t[1]] += 1
            else:
                ans.append(t[0])
                D[t[0]] += 1
                D[t[1]] -= 1

    print('Yes')
    for a in ans:
        if a == 0:
            print('A')
        elif a == 1:
            print('B')
        else:
            print('C')



def main():
    N, A, B, C = read_int_n()
    S = [read_str() for _ in range(N)]
    (slv(N, A, B, C, S))


    # N = 10**5
    # A = random.randint(1, 10**9)
    # B = random.randint(1, 10**9)
    # C = random.randint(1, 10**9)
    # S = random.choices(['AB', 'AC', 'BC'], k=N)
    # (slv(N, A, B, C, S))

if __name__ == '__main__':
    main()
