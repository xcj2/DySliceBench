# -*- coding: utf-8 -*-
# import bisect
# import heapq
# import math
# import random
# from collections import Counter, defaultdict, deque
# from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
# from fractions import Fraction
# from functools import lru_cache, reduce
# from itertools import combinations, combinations_with_replacement, product, permutations, accumulate
# from operator import add, mul, sub, itemgetter, attrgetter
from collections import defaultdict

import sys
# sys.setrecursionlimit(10**6)
readline = sys.stdin.buffer.readline
# readline = sys.stdin.readline

INF = 1 << 63


def read_int():
    return int(readline())


def read_int_n():
    return list(map(int, readline().split()))


def read_float():
    return float(readline())


def read_float_n():
    return list(map(float, readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


def ep(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.perf_counter()
        ret = f(*args, **kwargs)
        e = time.perf_counter()

        ep(e - s, 'sec')
        return ret

    return wrap


class SegmentTree:
    def __init__(self, array, operator, identity_element):
        _len = len(array)
        self.__len = _len
        self.__op = operator
        self.__size = 1 << (_len - 1).bit_length()
        self.__tree = [identity_element] * self.__size + \
            array + [identity_element] * (self.__size - _len)
        self.__ie = identity_element

        for i in range(self.__size - 1, 0, -1):
            self.__tree[i] = operator(
                self.__tree[i * 2], self.__tree[i * 2 + 1])

    def update(self, i, v):
        # ep('u', i, v)
        i += self.__size
        self.__tree[i] = v
        while i:
            i //= 2
            self.__tree[i] = self.__op(
                self.__tree[i * 2], self.__tree[i * 2 + 1])
        # ep(self.__tree[self.__size:])

    def query(self, l, r):
        """[l, r)
        """
        l += self.__size
        r += self.__size
        ret = self.__ie
        while l < r:
            if l & 1:
                ret = self.__op(ret, self.__tree[l])
                l += 1
            if r & 1:
                r -= 1
                ret = self.__op(ret, self.__tree[r])
            l //= 2
            r //= 2
        return ret

    def max_right(self, l, f):
        # https://atcoder.jp/contests/practice2/submissions/16636885
        assert 0 <= l <= self.__len
        if l == self.__len:
            return self.__len

        l += self.__size
        sm = self.__ie
        while True:
            while l % 2 == 0:
                l >>= 1
            if not f(self.__op(sm, self.__tree[l])):
                while l < self.__size:
                    l = 2*l
                    if f(self.__op(sm, self.__tree[l])):
                        sm = self.__op(sm, self.__tree[l])
                        l += 1
                return l - self.__size
            sm = self.__op(sm, self.__tree[l])
            l += 1

            if (l & -l) == l:
                break

        return self.__len

    def min_left(self, r, f):
        assert 0 <= r <= self.__len
        if r == 0:
            return 0

        r += self.__size
        sm = self.__ie
        while True:
            r -= 1
            while r > 1 and (r % 2):
                r >>= 1
            if not f(self.__op(sm, self.__tree[r])):
                while r < self.__size:
                    r = 2*r + 1
                    if f(self.__op(sm, self.__tree[r])):
                        sm = self.__op(sm, self.__tree[r])
                        r -= 1
                return r + 1 - self.__size
            sm = self.__op(sm, self.__tree[r])

            if (r & -r) == r:
                break

        return 0

    def __getitem__(self, key):
        return self.__tree[key + self.__size]

    def p(self):
        ep(self.__tree[self.__size:])


class UnionFind():
    def __init__(self):
        self.__table = {}
        self.__size = defaultdict(lambda: 1)
        self.__rank = defaultdict(lambda: 1)

    def __root(self, x):
        if x not in self.__table:
            self.__table[x] = x
            return x
        else:
            a = x
            ul = []
            while a != self.__table[a]:
                ul.append(a)
                a = self.__table[a]
            for u in ul:
                self.__table[u] = a

        return self.__table[x]

    def same(self, x, y):
        return self.__root(x) == self.__root(y)

    def union(self, x, y):
        # ep(x, y)
        x = self.__root(x)
        y = self.__root(y)
        if x == y:
            return False

        if self.__rank[x] < self.__rank[y]:
            self.__table[x] = y
            self.__size[y] += self.__size[x]
        else:
            self.__table[y] = x
            self.__size[x] += self.__size[y]
            if self.__rank[x] == self.__rank[y]:
                self.__rank[x] += 1
        return True

    def size(self, x):
        return self.__size[self.__root(x)]

    def num_of_group(self):
        g = 0
        for k, v in self.__table.items():
            if k == v:
                g += 1
        return g


def ref(N, XY):

    uf = UnionFind()
    for i in range(N):
        xi, yi = XY[i]
        for j in range(i+1, N):
            xj, yj = XY[j]
            if xj < xi and yj < yi or xj > xi and yj > yi:
                uf.union(i, j)

    ans = [0] * N
    for i in range(N):
        ans[i] = uf.size(i)

    return ans


@mt
def slv(N, XY):
    xyi = [(x, y, i) for i, (x, y) in enumerate(XY)]
    xyi.sort()

    y2i = {}
    y2x = {}
    x2y = {}
    # ia = [INF] * (N+1)
    for x, y, i in xyi:
        y2i[y] = i
        y2x[y] = x
        x2y[x] = y
        # ia[y] = y
    ia = list(range(N+1))
    ia[0] = INF
    styr = SegmentTree(ia, min, INF)

    uf = UnionFind()
    for x, y, i in xyi:
        a = y
        mx = 0
        my = 0
        styr.update(y, INF)
        while True:
            v = styr.query(a+1, N+1)
            if v == INF:
                break
            j = y2i[v]
            uf.union(i, j)
            styr.update(v, INF)
            a = v
            mx = max(mx, y2x[v])
            my = max(my, v)

        if mx > x:
            styr.update(x2y[mx], my)
            y2i[my] = i

    ans = [0] * N
    for i in range(N):
        ans[i] = uf.size(i)

    return ans


def main():
    N = read_int()
    XY = [read_int_n() for _ in range(N)]
    print(*slv(N, XY), sep='\n')

    # from random import shuffle
    # N = 2 * 10**5
    # X = list(range(1, N+1))
    # Y = list(range(1, N+1))
    # shuffle(X)
    # shuffle(Y)
    # XY = list(zip(X, Y))
    # # XY = [(2, 5), (1, 3), (3, 2), (5, 1), (4, 4)]
    # b = slv(N, XY)

    # for _ in range(1000):
    #     from random import shuffle
    #     # N = 2 * 10**5
    #     N = 5
    #     X = list(range(1, N+1))
    #     Y = list(range(1, N+1))
    #     shuffle(X)
    #     shuffle(Y)
    #     XY = list(zip(X, Y))
    #     # XY = [(2, 5), (1, 3), (3, 2), (5, 1), (4, 4)]
    #     a = ref(N, XY)
    #     b = slv(N, XY)
    #     if a != b:
    #         ep('-----')
    #         ep(N)
    #         ep(XY)
    #         ep('a', a)
    #         ep('b', b)
    #         break


if __name__ == '__main__':
    main()
