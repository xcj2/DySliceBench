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


from  fractions import Fraction

def f(a, b):
    if a== 0 and b == 0:
        return (1, 0, 0)
    if b == 0:
        return (1, 1, 0)
    f = Fraction(a, b)
    a = f.numerator
    b = f.denominator
    if a < 0:
        s = -1
        a *= -1
    else:
        s = 1
    return s, a, b


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
def slv(N, AB):
    adb = Counter()
    for a, b in AB:
        s, a, b = f(a, b)
        adb[(s*a, b)] += 1
    M = Mod(1000000007)
    ans = 1
    done = set()
    for k, v in adb.items():
        if k in done:
            continue
        if k == (0, 0):
            continue
        a, b = k
        if a < 0:
            s = 1
            a = abs(a)
        elif a == 0:
            s = 1
        else:
            s = -1
        n = adb[(s*b, a)]
        done.add(k)
        done.add((s*b, a))
        t = M.sub(M.pow(2, v) + M.pow(2, n), 1)
        ans = M.mul(ans, t)

    return M.add(M.sub(ans, 1), adb[(0, 0)])


def main():
    N = read_int()
    AB = [read_int_n() for _ in range(N)]
    print(slv(N, AB))


if __name__ == '__main__':
    main()
