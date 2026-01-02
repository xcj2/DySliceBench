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
    N = int(input())
    P = li_input()

    ans = 0

    for i in range(len(P) - 1):
        if i + 1 != P[i]:
            continue

        P[i], P[i + 1] = P[i + 1], P[i]
        ans += 1

    if P[len(P) - 1] == len(P):
        ans += 1

    print(ans)


main()
