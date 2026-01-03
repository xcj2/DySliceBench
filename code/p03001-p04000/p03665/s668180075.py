#!/usr/bin/env python3
import math
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    n, p = MI()
    a = LI()
    num_0 = 0
    num_1 = 0
    for i in range(n):
        if a[i] % 2 == 0:
            num_0 += 1
        else:
            num_1 += 1

    s_1 = 0
    while p <= num_1:
        cmb = math.factorial(num_1) // (
            math.factorial(num_1 - p) * math.factorial(p)
        )
        s_1 += cmb
        p += 2

    print(s_1 * (2 ** num_0))


main()
