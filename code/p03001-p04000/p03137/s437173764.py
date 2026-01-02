#!/usr/bin/env python3
import sys
import math
import decimal
import itertools
from itertools import product
from functools import reduce


def main():
    N, M = map(int, input().split())
    X = sorted(list(map(int, input().split())))

    if N >= M:
        print(0)
        exit()

    d = []
    for i in range(M - 1):
        d.append(X[i + 1] - X[i])
    d = sorted(d, reverse=True)

    print(sum(d[N - 1:]))


def input():
    return sys.stdin.readline()[:-1]


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def sort_zip(a: list, b: list):
    z = zip(a, b)
    z = sorted(z)
    a, b = zip(*z)
    a = list(a)
    b = list(b)
    return a, b


if __name__ == '__main__':
    main()
