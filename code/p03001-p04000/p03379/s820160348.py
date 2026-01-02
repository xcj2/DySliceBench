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
    N = int(input())
    X = li_input()

    sX = sorted(X)
    med = sX[len(sX) // 2]
    med_min = sX[len(sX) // 2 - 1]

    for x in X:
        if x < med:
            print(med)
        else:
            print(med_min)


main()
