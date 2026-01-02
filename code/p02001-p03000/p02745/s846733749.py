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


@mt
def slv(A, B, C):
    @lru_cache(maxsize=None)
    def g(x, y):
        m = []
        for i in range(len(x)):
            for j in range(min(len(y), len(x)-i)):
                if not (x[i+j] == '?' or y[j] == '?' or x[i+j] == y[j]):
                    break
            else:
                m.append(i)
        m.append(len(x))
        return m

    def f(x, y, z):
        N = len(x) + len(y) + len(z)
        ans = N
        xy = g(x, y)
        yz = g(y, z)
        xz = g(x, z)
        # print(xy, yz, xz)
        xz_set = set(xz)
        for i in xy:
            for j in yz:
                if i + j < len(x) and i + j in xz_set:
                    s = max(i + len(y), i + j + len(z), len(x))
                elif i + j < len(x) and i + len(y) :
                    l = bisect.bisect_left(xz, i+len(y))
                    if l >= len(xz):
                        continue
                    k = xz[l]
                    # print(k, xz)
                    s = max(i + len(y), k + len(z), len(x))
                elif  i + j >= len(x):
                    s = max(i + len(y), i + j + len(z), len(x))
                else:
                    continue
                # print(x, y, z, i, j, s)
                ans = min(ans, s)
        return ans

    ans = INF
    for a, b, c in permutations((A, B, C)):
        ans = min(ans, f(a, b, c))

    return ans


def ref(A, B, C):
    def f(x, y):
        for i in range(len(x)):
            for j in range(min(len(y), len(x)-i)):
                if not (x[i+j] == '?' or y[j] == '?' or x[i+j] == y[j]):
                    break
            else:
                if len(y) > len(x)-i:
                    s = x + y[len(x)-i:]
                    s = list(s)
                    for j in range(len(x)-i):
                        if (x[i+j] == '?' and y[j] != '?'):
                            s[i+j] = y[j]
                    yield ''.join(s)
                else:
                    s = list(x)
                    for j in range(len(y)):
                        if (x[i+j] == '?' and y[j] != '?'):
                            s[i+j] = y[j]
                    yield ''.join(s)
        yield x + y
    ans = INF
    for x, y, z in permutations((A, B, C)):
        # print('-----', x, y, z)
        for xy in f(x, y):
            for xyz in f(xy, z):
                # print(xyz, len(xyz), xy)
                ans = min(ans, len(xyz))
    return ans

def main():
    A = read_str()
    B = read_str()
    C = read_str()
    print(slv(A, B, C))
    # print(ref(A, B, C))


    # # A, B, C = ['b', 'cacdd', 'b']
    # # A, B, C = ['d', 'acadcdac', 'ca']
    # # A, B, C = ['ab?b', 'bb', 'bc?']
    # # A, B, C = ['?aaa', 'b?ac', 'b?a?a']
    # # A, B, C = ['acb', 'b??bc', 'cccbc?b']
    # A, B, C = ['?bbbb', 'aa', 'cccba?ca']
    # # A, B, C = ['abba', '?cb', 'ccacba?a']
    # print(slv(A, B, C))
    # print(ref(A, B, C))



    # D = '?'*2000
    # print(slv(D, D, D))

    # for _ in range(10000):
    #     cs = 'abc?'
    #     A = ''.join(random.choices(cs, k=random.randint(1, 10)))
    #     B = ''.join(random.choices(cs, k=random.randint(1, 10)))
    #     C = ''.join(random.choices(cs, k=random.randint(1, 10)))
    #     a = slv(A, B, C)
    #     b = ref(A, B, C)
    #     if a != b:
    #         print(A)
    #         print(B)
    #         print(C)
    #         print(a, b)
    #         break


if __name__ == '__main__':
    main()
