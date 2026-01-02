#!/usr/bin/env python3
import sys


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()
    A = LI()
    A.sort()
    MAX = A[-1]+1
    All = [0 for i in range(MAX)]

    setA = set(A)
    for i in A:
        k = i
        All[k] += 1
        k += i
        if All[i] == 2:
            continue
        while k < MAX and i in setA:
            All[k] += 1
            k += i

    ans = 0
    for i in range(1, MAX):
        if All[i] == 1 and i in setA:
            ans += 1

    print(ans)

    # oj t -c "pypy3 main.py"
    # acc s main.py -- --guess-python-interpreter pypy
main()
