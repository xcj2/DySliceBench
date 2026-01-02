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


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def main():
    N = int(input())
    A = li_input()

    A.sort(reverse=True)
    ans_c = -1

    n = A[0]

    half = n / 2
    diff = 10 ** 100

    A.remove(n)

    for a in A:
        if abs(a - half) < diff:
            r = a
            diff = abs(a - half)

    print(n, r)


main()
