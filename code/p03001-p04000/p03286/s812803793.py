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
c = []


def f(B):
    ans = 0
    for idx in range(len(B)):
        if B[len(B) - idx - 1] == "1":
            ans += ((-2)**idx)

    return ans


def is_lower(idx, c_value, N):
    add_value = 0
    for i in range(idx, -1, -1):
        if c[i] > 0:
            add_value += c[i]

    return c_value + add_value < N


# idx未満の添え字の数を引いて行った結果，
# 目的の数を上回ればidxを引く必要がある
def is_over(idx, c_value, N):
    sub_value = 0
    for i in range(idx, -1, -1):
        if c[i] < 0:
            sub_value += c[i]

    return c_value + sub_value > N


def main():
    N = int(input())
    c_value = None

    if N == 0:
        print(0)
        return

    for i in range(50):
        c.append((-2)**i)

    if N > 0:
        tmpsum = 0
        for i in range(50):
            if c[i] > 0:
                tmpsum += c[i]

            if tmpsum >= N:
                idx = i
                c_value = c[i]
                break

        ans = "1"

        for c_idx in range(idx - 1, -1, -1):
            if c[c_idx] < 0:
                if is_over(c_idx - 2, c_value, N):
                    ans += "1"
                    c_value += c[c_idx]
                else:
                    ans += "0"
            else:
                if is_lower(c_idx - 2, c_value, N):
                    ans += "1"
                    c_value += c[c_idx]
                else:
                    ans += "0"

    else:
        tmpsub = 0
        for i in range(50):
            if c[i] < 0:
                tmpsub += c[i]

            if tmpsub <= N:
                idx = i
                c_value = c[i]
                break

        ans = "1"

        for c_idx in range(idx - 1, -1, -1):
            if c[c_idx] < 0:
                if is_over(c_idx - 2, c_value, N):
                    ans += "1"
                    c_value += c[c_idx]
                else:
                    ans += "0"
            else:
                if is_lower(c_idx - 2, c_value, N):
                    ans += "1"
                    c_value += c[c_idx]
                else:
                    ans += "0"

    print(ans)


main()
