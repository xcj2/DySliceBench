#!/usr/bin/env python3

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


def main():
    x = I()

    yen500 = x // 500
    yen5 = (x - 500 * yen500) // 5

    ans = yen500 * 1000 + yen5 * 5

    print(ans)


main()
