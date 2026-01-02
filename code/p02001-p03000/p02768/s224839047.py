# import numpy as np
# import math
# import copy
# from collections import deque
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10000)
from math import factorial


def comb(n,k,p):
    if n<0 or k<0 or n<k: return 0
    if n==0 or k==0: return 1
    mink = min(k,n-k)
    a = 1
    b = 1
    for i in range(mink):
        a = a * (n-i) % p
        b = b * (i+1) % p

    return (a*power_func(b,p-2,p))%p


def power_func(a,b,p):
    if b==0: return 1
    if b%2==0:
        d=power_func(a,b//2,p)
        return d*d %p
    if b%2==1:
        return (a*power_func(a,b-1,p ))%p


def main():
    n,a,b = map(int,input().split())

    mod = 10 ** 9 + 7

    temp1 = comb(n,a,mod)
    temp2 = comb(n,b,mod)

    res = power_func(2,n,mod) - 1
    res -= temp1 + temp2
    res %= mod

    print(res)



main()
