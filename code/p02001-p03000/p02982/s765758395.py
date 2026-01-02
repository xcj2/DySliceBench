#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from math import sqrt

def rl(proc=None):
    if proc is not None:
        return proc(sys.stdin.readline())
    else:
        return sys.stdin.readline().rstrip()

def srl(proc=None):
    if proc is not None:
        return list(map(proc, rl().split()))
    else:
        return rl().split()

def dist(a, b):
    r = 0
    for i in range(len(a)):
        d = a[i] - b[i]
        r += d * d
    return r

def issq(d):
    c = int(sqrt(d))
    return c * c == d or (c+1) * (c+1) == d

def main():
    N, D = srl(int)
    A = []
    for _ in range(N):
        A.append(srl(int))
    c = 0
    for i in range(N):
        for j in range(i+1, N):
            if issq(dist(A[i], A[j])):
                c += 1
    print(c)

if __name__ == '__main__':
    main()
