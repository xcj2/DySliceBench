#!/usr/bin/env python3
import sys
import math
import decimal
import itertools
from itertools import product
from functools import reduce
def input():
    return sys.stdin.readline()[:-1]
def sort_zip(a:list, b:list):
    z = zip(a, b)
    z = sorted(z)
    a, b = zip(*z)
    a = list(a)
    b = list(b)
    return a, b

def warikirenai(n, warukazu):
    return n - n // warukazu
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def main():
    A, B, C, D = map(int, input().split())

    ansA = 0
    ansA += warikirenai(A - 1, C)
    ansA += warikirenai(A - 1, D)
    ansA -= warikirenai(A - 1, lcm(C, D))

    ansB = 0
    ansB += warikirenai(B, C)
    ansB += warikirenai(B, D)
    ansB -= warikirenai(B, lcm(C, D))

    print(ansB - ansA)


if __name__ == '__main__':
    main()
