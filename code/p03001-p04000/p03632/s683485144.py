import sys
import math
import collections
import itertools
import array
import inspect

# Set max recursion limit
sys.setrecursionlimit(10000)


# Debug output
def chkprint(*args):
    names = {
        id(v): k
        for k, v in inspect.currentframe().f_back.f_locals.items()
    }
    print(', '.join(
        names.get(id(arg), '???') + ' = ' + repr(arg) for arg in args))


# Binary converter
def to_bin(x):
    return bin(x)[2:]


def li_input():
    return [int(_) for _ in input().split()]


# --------------------------------------------

dp = None


def main():
    A, B, C, D = li_input()
    L = [0] * 101

    for i in range(101):
        if A <= i < B:
            L[i] += 1

        if C <= i < D:
            L[i] += 1

    ans = 0

    for l in L:
        if l == 2:
            ans += 1

    print(ans)


main()
