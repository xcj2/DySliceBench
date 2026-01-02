#!/usr/bin/env python3
import sys
from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    n, m, k = MI()
    a = deque(LI())
    b = deque(LI())

    A, B = [0], [0]

    for i in range(len(a)):
        A.append(A[i]+a[i])
    for i in range(len(b)):
        B.append(B[i]+b[i])

    index = m
    ans = [0]
    for i in range(len(a)+1):
        rest = k - A[i]
        if rest < 0:
            break

        while B[index] > rest:
            index -= 1

        ans.append(i + index)

    print(max(ans))


    # oj t -c "pypy3 main.py"
    # acc s main.py -- --guess-python-interpreter pypy
main()
