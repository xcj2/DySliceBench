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
    N, C = li_input()

    A = [[0] * 100001 for _ in range(C)]
    S = [0] * 100001

    for i in range(N):
        s, t, c = li_input()

        for j in range(s, t):
            A[c - 1][j] += 1

    for a in A:
        for i in range(1, len(a)):
            if a[i] == 1 or (i != len(a) - 1 and a[i + 1]) == 1:
                S[i] += 1

    print(max(S))


main()
