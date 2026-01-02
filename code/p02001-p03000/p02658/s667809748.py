#!/usr/bin/env python3
import sys


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()
    A = LI()

    ans = 1
    index = 0
    A_set = set(A)
    if 0 in A_set:
        print(0)
        return
    while index < N:
        ans *= A[index]
        index += 1
        if ans > 10**18:
            break

    if ans <= 10**18:
        print(ans)
    else:
        print(-1)


# oj t -c "pypy3 main.py"
# acc s main.py -- --guess-python-interpreter pypy
main()
