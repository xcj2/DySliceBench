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

def main():
    L, R = map(int, input().split())

    for i in range(1, 990589):
        if L <= 2019*i <= R:
            print(0)
            exit()

    ans = 10**19
    for i in range(L, R):
        for j in range(L + 1, R + 1):
            num = (i * j) % 2019
            ans = min(ans, num)
    print(ans)


if __name__ == '__main__':
    main()
