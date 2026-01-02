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
    k = I()
    numlist = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]
    print(numlist[k - 1])


main()
