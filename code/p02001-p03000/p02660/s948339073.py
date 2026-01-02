# -*- coding: utf-8 -*-
from collections import Counter, defaultdict, deque
import math
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


def eratosthenes(n):
    p = []
    t = [True] * n

    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if t[i]:
            p.append(i)
            for j in range(2*i, n, i):
                t[j] = False

    for j in range(i+1, n):
        if t[j]:
            p.append(j)

    return p

P = eratosthenes(10**6+1)


class Bisect:
    def __init__(self, func):
        self.__func = func

    def bisect_left(self, x, lo, hi):
        while lo < hi:
            mid = (lo+hi)//2
            if self.__func(mid) < x:
                lo = mid+1
            else:
                hi = mid
        return lo

    def bisect_right(self, x, lo, hi):
        while lo < hi:
            mid = (lo+hi)//2
            if x < self.__func(mid):
                hi = mid
            else:
                lo = mid+1
        return lo

def f(n):
    return (n**2 + n) // 2

@mt
def slv(N):
    if N == 1:
        return 0

    d = Counter()
    for p in P:
        n = 0
        while N % p == 0:
            n += 1
            N //= p
        if n != 0:
            d[p] = n
        if N == 1:
            break
    if N != 1:
        d[N] = 1
    ans = 0
    for p, n in d.items():
        i = Bisect(f).bisect_left(n+1, 0, 10**18)-1
        ans += i

    return ans


def main():
    N = read_int()
    print(slv(N))


if __name__ == '__main__':
    main()
