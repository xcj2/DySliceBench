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
    t = 0
    A = li_input()

    while max(A) - min(A) > 1:
        t += 1
        A[A.index(min(A))] += 2

    if A.count(max(A)) == 2:
        t += 2
    elif A.count(max(A)) == 1:
        t += 1

    print(t)


main()
