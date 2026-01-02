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


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)
def warikirenai(n, c, d):
    num =  n - n // c
    num += n - n // d
    num -= n - n // lcm(c, d)
    return num

def main():
    A, B, C, D = map(int, input().split())

    print(warikirenai(B, C, D) - warikirenai(A - 1, C, D))


if __name__ == '__main__':
    main()
