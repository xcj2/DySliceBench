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
    N, H = li_input()
    S = [li_input() for _ in range(N)]

    ans = 0
    strong_throw = []

    maxcut = -1
    for s in S:
        if s[0] > maxcut:
            maxcut = s[0]

    for s in S:
        if s[1] > maxcut:
            strong_throw.append(s[1])

    strong_throw.sort(reverse=True)

    for st in strong_throw:
        H -= st
        ans += 1

        if H <= 0:
            break

    if H > 0:
        ans += math.ceil(H / maxcut)

    print(ans)


main()
