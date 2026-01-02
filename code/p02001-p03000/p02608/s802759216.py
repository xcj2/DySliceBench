#!/usr/bin/env python3
import sys
import math
import collections


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()
    list_counter = collections.Counter()

    for i in range(1, math.floor(N**(1/2))+1):
        for j in range(1,  math.floor(N**(1/2))+1):
            for k in range(1,  math.floor(N**(1/2))+1):
                n = i**2 + j**2 + k**2 + i*j + j*k + k*i
                list_counter.update({n: 1})

    for n in range(1, N+1):
        print(list_counter[n])


    # oj t -c "pypy3 main.py"
    # acc s main.py -- --guess-python-interpreter pypy
main()
