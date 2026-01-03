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
    A = li_input()
    D = collections.defaultdict(lambda: 0)
    C = [0, 0]

    for a in A:
        D[a] += 1

    for k, v in D.items():
        if 2 <= v:
            C.append(k)
        if 4 <= v:
            C.append(k)

    C.sort(reverse=True)

    print(C[0] * C[1])


main()
