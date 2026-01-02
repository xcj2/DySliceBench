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
    names = {id(v): k for k, v in inspect.currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg), '???')+' = '+repr(arg) for arg in args))

# Binary converter


def to_bin(x):
    return bin(x)[2:]


def li_input():
    return [int(_) for _ in input().split()]

# --------------------------------------------


dp = None


def main():
    N, M, X = li_input()
    A = li_input()

    C = []
    for i in range(N + 1):
        if i in A:
            C.append(1)
        else:
            C.append(0)

    print(min(
        sum(C[:X]),
        sum(C[X+1:])
    ))


main()
