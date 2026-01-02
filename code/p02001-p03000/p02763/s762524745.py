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
from operator import add, mul, sub, or_

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


class SegmentTree():
    # to par: (n-1) // 2
    # to chr: 2n+1, 2n+2
    def __init__(self, array, operator, identity_element):
        """ operator and identity_element has to be a monoid.
        """
        self.__N = 2**int(math.ceil(math.log(len(array), 2)))
        self.__table = [identity_element] * (self.__N * 2 - 1)
        self.__op = operator
        self.__ie = identity_element
        for i, v in enumerate(array):
            self.__table[i+self.__N - 1] = v

        for i in range(self.__N - 2, 0, -1):
            pi = i
            li = 2*pi + 1
            ri = 2*pi + 2
            v = self.__op(self.__table[li], self.__table[ri])
            self.__table[pi] = v


    def update(self, idx, x):
        i = self.__N - 1 + idx  # target leaf
        t = self.__table
        o = self.__op

        t[i] = x
        while i != 0:
            pi = (i - 1) // 2  # parent
            li = 2*pi + 1
            ri = 2*pi + 2
            v = o(t[li], t[ri])
            t[pi] = v
            i = pi

    def query(self, a, b):
        stack = [(0, 0, self.__N)]
        t = self.__table
        o = self.__op

        ans = self.__ie
        c = 0
        while stack:
            c += 1
            k, l, r = stack.pop()
            cnd = t[k]
            if a <= l and r <= b:
                ans = o(ans, cnd)
            else:
                if (l + r) // 2 > a and b > l:
                    stack.append((2 * k + 1, l, (l + r) // 2))

                if r > a and b > (l + r) // 2:
                    stack.append((2 * k + 2, (l + r) // 2, r))
        return ans

    def print(self):
        print(self.__table)



@mt
def slv(N, S, Q):
    st = SegmentTree([1 << (ord(c) - ord('a')) for c in S], or_, 0)

    for q in Q:
        if q[0] == '1':
            i = int(q[1]) - 1
            c = q[2]
            st.update(i, 1 << (ord(c) - ord('a')))
        if q[0] == '2':
            i = int(q[1]) - 1
            j = int(q[2]) - 1
            ans = 0
            v = st.query(i, j+1)
            for k in range(26):
                if (1 << k) & v:
                    ans += 1
            print(ans)
    # return ans


def main():
    N = read_int()
    S = read_str()
    Q = [read_str_n() for _ in range(read_int())]
    (slv(N, S, Q))

if __name__ == '__main__':
    main()
