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

    ans = 0

    while True:
        A_ = []
        is_end = False

        for a in A:
            if a % 2 != 0:
                is_end = True
                break
            else:
                A_.append(a // 2)

        if is_end:
            break
        else:
            ans += 1
            A = A_[:]

    print(ans)


main()
