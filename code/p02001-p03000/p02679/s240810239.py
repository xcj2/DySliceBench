# -*- coding: utf-8 -*-
from fractions import Fraction
from collections import Counter
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


def fract(a, b):
    if a == 0 and b == 0:
        return (0, 0)
    if b == 0:
        return (1, 0)
    f = Fraction(a, b)
    return f.numerator, f.denominator


@mt
def slv(N, AB):
    adb = Counter()
    for a, b in AB:
        k = fract(a, b)
        adb[k] += 1
    M = Mod(1000000007)
    ans = 1
    done = {(0, 0)}
    for k, v in adb.items():
        if k in done:
            continue
        a, b = k
        kk = fract(-b, a)
        done.add(k)
        done.add(kk)

        n = adb[kk]
        t = M.sub(M.pow(2, v) + M.pow(2, n), 1)
        ans = M.mul(ans, t)
    ans = M.add(ans, adb[(0, 0)])
    return M.sub(ans, 1)


def main():
    N = read_int()
    AB = [read_int_n() for _ in range(N)]
    print(slv(N, AB))


if __name__ == '__main__':
    main()
