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

class LazySegmentTree():
    def __init__(self, f, g, h, f_ie, g_ie, init_array):
        self.f = f
        self.g = g
        self.h = h
        self.f_ie = f_ie
        self.g_ie = g_ie

        l = len(init_array)
        self.size = 1 << (l - 1).bit_length()
        self.hight = self.size.bit_length()
        self.tree = [f_ie] * self.size + init_array + [f_ie] * (self.size - l)
        self.lazy = [g_ie] * (self.size * 2)

        self.chn = [0] * (self.size * 2)
        for i in range(self.size, self.size+l):
            self.chn[i] = 1
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = f(self.tree[i << 1], self.tree[(i << 1) | 1])
            self.chn[i] = self.chn[i << 1] + self.chn[(i << 1) | 1]

    def reflect(self, k):
        return self.tree[k] if self.lazy[k] == self.g_ie else self.g(self.tree[k], self.lazy[k], self.chn[k])

    def propagate(self, k):
        if self.lazy[k] == self.g_ie:
            return
        self.lazy[(k << 1) | 0] = self.h(self.lazy[(k << 1) | 0], self.lazy[k])
        self.lazy[(k << 1) | 1] = self.h(self.lazy[(k << 1) | 1], self.lazy[k])
        self.tree[k] = self.reflect(k)
        self.lazy[k] = self.g_ie

    def thrust(self, k):
        for i in range(self.hight, 0, -1):
            self.propagate(k >> i)

    def calc(self, k):
        while k != 0:
            k >>= 1
            self.tree[k] = self.f(self.reflect(
                k << 1), self.reflect((k << 1) | 1))

    def update(self, l, r, x):
        if l >= r:
            return

        l += self.size
        r += self.size

        self.thrust(l)
        self.thrust(r-1)

        a = l
        b = r
        while l < r:
            if l & 1:
                self.lazy[l] = self.h(self.lazy[l], x)
                l += 1
            if r & 1:
                r -= 1
                self.lazy[r] = self.h(self.lazy[r], x)
            l >>= 1
            r >>= 1
        self.calc(a)
        self.calc(b-1)

    def query(self, l, r):
        """
        reduce(f, a[l:r], ie)
        """

        if l >= r:
            return self.f_ie

        l += self.size
        r += self.size
        self.thrust(l)
        self.thrust(r-1)

        vl = self.f_ie
        vr = self.f_ie
        while l < r:
            if l & 1:
                vl = self.f(vl, self.reflect(l))
                l += 1
            if r & 1:
                 r -= 1
                 vr = self.f(self.reflect(r), vr)
            l >>= 1
            r >>= 1
        return self.f(vl, vr)

    def __print(self, a):
        cl = max(map(lambda x: len(str(x)), a[1:]))
        p = (r'|%' + str(cl) + r's')
        cl += 1
        for i in range(self.hight):
            j = 1 << i
            bc = (1 << (self.hight-i-1)) - 1
            s = ' ' + ' ' * ((cl+1) * bc)
            print(s.join(map(lambda x: p % x, a[j:j*2])))

    def print(self):
        print('tree')
        self.__print(self.tree)
        print('lazy')
        self.__print(self.lazy)


@mt
def slv(N, K, A):

    AA = A[:]
    from itertools import accumulate
    for _ in range(K):
        sa = [0] * N
        for i, d in enumerate(AA):
            sa[max(0, i-d)] += 1
            if i+d+1 < N:
                sa[i+d+1] -= 1
        AA = list(accumulate(sa))
        if min(AA) == N:
            break
    return AA


def main():
    N, K = read_int_n()
    A = read_int_n()
    print(*slv(N, K, A))


    # N = 2*(10**5)
    # K = 2*(10**5)
    # A = [0] * N
    # print(*slv(N, K, A))


if __name__ == '__main__':
    main()
