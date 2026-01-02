# -*- coding: utf-8 -*-
import math
import operator
from functools import reduce
def gcd(a,b):
    c = 0
    while a != b:
        if a&1==b&1==0:
            a, b = a>>1, b>>1
            c += 1
        elif min(a,b) == 0:
            a = max(a,b)
        else:
            a, b = max(a,b)%min(a,b), min(a,b)
    return a*2**c


def lcm(a,b):
    return (a*b)//gcd(a,b)

def solve():
    N = int(input())
    *A, = map(int, input().split())
    m = reduce(lcm, A) - 1
    s = sum([m%a for a in A])

    return str(s)

if __name__ == '__main__':
    print(solve())
