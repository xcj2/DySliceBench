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


class Mod:
    def __init__(self, m):
        self.m = m

    def add(self, a, b):
        return (a + b) % self.m

    def sub(self, a, b):
        return (a - b) % self.m

    def mul(self, a, b):
        return ((a % self.m) * (b % self.m)) % self.m

    def div(self, a, b):
        return self.mul(a, pow(b, self.m-2, self.m))

    def pow(self, a, b):
        return pow(a, b, self.m)



@mt
def slv(N, K, A):
    M = 10**9+7

    def p(N, K, A):
        pa = [a for a in A if a >= 0]
        na = [-a for a in A if a < 0]
        # positive
        pa.sort()
        na.sort()
        ans = 1
        if K % 2 == 1:
            if len(pa) == 0:
                return None
            ans *= pa.pop()
            K -= 1
        for _ in range(K//2):
            if len(pa) >= 2 and len(na) >= 2:
                if pa[-1] * pa[-2] > na[-1] * na[-2]:
                    ans *= pa[-1] * pa[-2]
                    pa.pop()
                    pa.pop()
                else:
                    ans *= na[-1] * na[-2]
                    na.pop()
                    na.pop()
            elif len(pa) >= 2:
                ans *= pa[-1] * pa[-2]
                pa.pop()
                pa.pop()
            elif len(na) >= 2:
                ans *= na[-1] * na[-2]
                na.pop()
                na.pop()
            else:
                break
            ans %= M
        else:
            return ans
        return None

    def n(N, K, A):
        pa = [a for a in A if a >= 0]
        na = [-a for a in A if a < 0]
        # negative
        pa.sort(reverse=True)
        na.sort(reverse=True)
        ans = 1
        for _ in range(K):
            if pa and na:
                if pa < na:
                    ans *= pa[-1]
                    pa.pop()
                else:
                    ans *= -na[-1]
                    na.pop()
            elif pa:
                ans *= pa[-1]
                pa.pop()
            else:
                ans *= -na[-1]
                na.pop()
            ans %= M
        return ans

    a = p(N, K, A)
    if a:
        return a
    return n(N, K, A)


def main():
    N, K = read_int_n()
    A = read_int_n()
    print(slv(N, K, A))

    import random
    # N = random.choice([9, 10])
    # K = random.randint(1, N)
    # A = [random.randint(-20, 20) for _  in range(N)]

    # N = 9
    # K = 9
    # A = [4, -9, -18, 7, 3, -5, -15, 14, -20]
    # print(N, K)
    # print(A)
    # print(slv(N, K, A))


if __name__ == '__main__':
    main()
