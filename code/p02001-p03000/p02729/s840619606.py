#!/usr/bin/env python3

import math
import sys


def LI():
    return list(map(int, sys.stdin.buffer.readline().split()))


def I():
    return int(sys.stdin.buffer.readline())


def LS():
    return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()


def S():
    return sys.stdin.buffer.readline().rstrip().decode('utf-8')


def IR(n):
    return [I() for i in range(n)]


def LIR(n):
    return [LI() for i in range(n)]


def SR(n):
    return [S() for i in range(n)]


def LSR(n):
    return [LS() for i in range(n)]


def SRL(n):
    return [list(S()) for i in range(n)]


def MSRL(n):
    return [[int(j) for j in list(S())] for i in range(n)]

# ----------------------------------------------------------------


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def main():
    n, m = LI()

    if n + m < 2:
        print(0)
        sys.exit

    ans = 0
    if n >= 2:
        ans += combinations_count(n, 2)
    if m >= 2:
        ans += combinations_count(m, 2)

    print(ans)


main()
