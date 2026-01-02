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


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def main():
    N = get_input(int)
    AB = []
    for _ in range(N):
        A, B = get_inputs(int)
        AB.append((A, B))
    AB.sort(key=lambda x: x[1])

    cur_time = 0
    for A, B in AB:
        cur_time += A
        if cur_time > B:
            print('No')
            return
    print('Yes')
    return


if __name__ == '__main__':
    main()
