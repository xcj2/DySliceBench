#!/usr/bin/env python
from collections import defaultdict, deque
import math
from math import factorial
import fractions
import re

BIGNUM = 10 ** 9 + 7

def convtobit(x):
    b = bin(x)
    bits = list(map(int, b[2:]))
    bits = [0] * (32 - len(bits)) + bits
    return tuple(bits)

def minus(x, y):
    b = []
    for xb, yb in zip(x, y):
        bit = 1 if xb != yb else 0
        b.append(bit)
    return tuple(b)

def main():
    #A, B, C, K = map(int, input().split())
    N = int(input())
    As = list(map(int, input().split()))

    # find N-th and 2nd number
    Adict = defaultdict(int)
    for a in As:
        b = convtobit(a)
        Adict[b] += 1

    assert convtobit(2) == tuple([0]*30 + [1, 0])
    assert convtobit(7) == tuple([0]*29 + [1, 1, 1])

    if len(Adict) > 3:
        print("No")
        return

    for first in Adict:
        for second in Adict:
            third = minus(first, second)
            if not third in Adict:
                continue
            forth = minus(second, third)
            if forth != first:
                continue

            if N % 3 == 0:
                adict = dict(Adict)
                for elem in [first, second, third]:
                    adict[elem] -= N // 3
                if all([adict[elem] == 0 for elem in [first, second, third]]):
                    print("Yes")
                    return

            if N % 3 == 1:
                adict = dict(Adict)
                for elem in [first, second, third]:
                    adict[elem] -= (N - 1) // 3
                adict[first] -= 1
                if all([adict[elem] == 0 for elem in [first, second, third]]):
                    print("Yes")
                    return

            if N % 3 == 2:
                adict = dict(Adict)
                for elem in [first, second, third]:
                    adict[elem] -= (N - 2) // 3
                adict[first] -= 1
                adict[second] -= 1
                if all([adict[elem] == 0 for elem in [first, second, third]]):
                    print("Yes")
                    return

    print("No")

if __name__ == '__main__':
    main()
