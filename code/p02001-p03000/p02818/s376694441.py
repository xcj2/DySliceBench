# -*- coding: utf-8 -*-
# abc149/abc149_b
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
    A, B, K = i2nn()
    if A > K:
        print(A - K, B)
    elif A + B > K:
        print(0, B + A - K)
    else:
        print(0, 0)
    return


main()
