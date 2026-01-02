#!/usr/bin/env python3
import sys
import math
import collections


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()
    ans = 0
    list_counter = []

    for i in range(1, math.floor(N**(1/2))+1):
        for j in range(i,  math.floor(N**(1/2))+1):
            for k in range(j,  math.floor(N**(1/2))+1):
                n = str(i**2 + j**2 + k**2 + i*j + j*k + k*i)
                tmp = set([i, j, k])

                if len(tmp) == 3:
                    tmp_list = [n]*6
                if len(tmp) == 2:
                    tmp_list = [n]*3
                if len(tmp) == 1:
                    tmp_list = [n]*1
                list_counter.extend(tmp_list)

    counter = collections.Counter(list_counter)
    for n in range(1, N+1):
        print(counter[str(n)])



    # oj t -c "pypy3 main.py"
    # acc s main.py -- --guess-python-interpreter pypy
main()
