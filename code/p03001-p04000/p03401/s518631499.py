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
    A.insert(0, 0)
    A.append(0)

    total = 0

    for i in range(1, len(A)):
        total += abs(A[i] - A[i - 1])

    for i in range(1, len(A) - 1):
        ans = total
        ans -= abs(A[i] - A[i - 1])
        ans -= abs(A[i + 1] - A[i])
        ans += abs(A[i + 1] - A[i - 1])
        print(ans)


main()
