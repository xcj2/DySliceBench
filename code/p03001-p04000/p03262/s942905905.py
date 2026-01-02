#!/usr/bin/env python3
import sys
import math
import decimal
import itertools
from itertools import product
from functools import reduce

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))

    x.append(X)
    x = sorted(x)

    d = []
    for i in range(N):
        d.append(x[i + 1] - x[i])

    print(gcd(*d))


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

if __name__ == '__main__':
    main()
