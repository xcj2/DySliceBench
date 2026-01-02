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
    A, B, K = li_input()

    C = []

    for i in range(A, min(A + K, B+1)):
        C.append(i)

    for i in range(max(A, B - K + 1), B + 1):
        if i not in C:
            C.append(i)

    for c in C:
        print(c)


main()
