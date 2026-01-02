#!/usr/bin/env python3
import sys
import math
import decimal
import itertools
from itertools import product
from functools import reduce
def input():
    return sys.stdin.readline()[:-1]
def gcd(*numbers):
    return reduce(math.gcd, numbers)
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)
def sort_zip(a:list, b:list):
    z = zip(a, b)
    z = sorted(z)
    a, b = zip(*z)
    a = list(a)
    b = list(b)
    return a, b
def ceil(x):
    return math.ceil(x)
def floor(x):
    return math.floor(x)

def main():
    N = int(input())
    abc= [list(map(int, input().split())) for _ in range(N)]

    A = [0]
    B = [0]
    C = [0]

    for i in range(N):
        a = max(B[-1], C[-1]) + abc[i][0]
        b = max(C[-1], A[-1]) + abc[i][1]
        c = max(A[-1], B[-1]) + abc[i][2]
        A.append(a)
        B.append(b)
        C.append(c)

    print(max(A[-1], B[-1], C[-1]))

if __name__ == '__main__':
    main()
