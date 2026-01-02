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
    s = S()

    n = len(s)
    a1 = int((n - 1) / 2)
    a2 = int((n + 3) / 2 - 1)
    pow1 = s[:a1]
    pow2 = s[a2:]

    if s == s[::-1] and pow1 == pow1[::-1] and pow2 == pow2[::-1]:
        print("Yes")

    else:
        print("No")


main()
