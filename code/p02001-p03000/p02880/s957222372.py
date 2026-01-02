# -*- coding: utf-8 -*-
# abc144/abc144_b
import sys


def s2nn(s): return [int(c) for c in s.split(' ')]


def ss2nn(ss): return [int(s) for s in list(ss)]


def ss2nnn(ss): return [s2nn(s) for s in list(ss)]


def i2s(): return sys.stdin.readline().rstrip()


def i2n(): return int(i2s())


def i2nn(): return s2nn(i2s())


def ii2ss(n): return [i2s() for _ in range(n)]


def ii2nn(n): return ss2nn(ii2ss(n))


def ii2nnn(n): return ss2nnn(ii2ss(n))


def main():
    N = i2n()
    s = set(range(1, 10))
    for i in range(1, 10):
        if (N/i in s):
            print('Yes')
            return
    print('No')
    return


main()
