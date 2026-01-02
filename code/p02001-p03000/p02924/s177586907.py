import collections
import math
import operator as op
from functools import reduce
import numpy as np
import math
import bisect
import heapq


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def get_inputs(cast_func=None):
    if cast_func is None:
        return input().split()
    else:
        return list(map(cast_func, input().split()))


def get_input(cast_func=None):
    if cast_func is None:
        return input()
    else:
        return cast_func(input())


def main():
    N = get_input(int)
    print(N * (N - 1) // 2)


if __name__ == '__main__':
    main()
