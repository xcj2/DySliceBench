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
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    count = 0
    for i in range(N):
        if A[i] == B[i]:
            count += 1
            if count == 3:
                print('Yes')
                exit()
        else:
            count = 0
    print('No')



if __name__ == '__main__':
    main()
