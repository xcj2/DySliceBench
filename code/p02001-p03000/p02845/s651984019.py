#!/usr/bin/python3

import os
import sys


def main():
    N = read_int()
    A = read_ints()
    print(solve(N, A))


MOD = 1000000007


def solve(N, A):
    c = 1
    nums = [0, 0, 0]

    for a in A:
        z = nums.count(a)
        if z == 0:
            return 0
        c *= z
        c %= MOD
        nums[nums.index(a)] = a + 1

    return c


###############################################################################

DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


if __name__ == '__main__':
    main()
