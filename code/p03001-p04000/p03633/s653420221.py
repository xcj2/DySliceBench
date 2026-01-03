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


def gcd(n, m):
    if n % m == 0:
        return m
    else:
        return gcd(m, n % m)


def lcm(n, m):
    return (n * m) // gcd(n, m)


def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]

    ans = 1

    for i in range(N):
        ans = lcm(ans, T[i])

    print(ans)


main()
