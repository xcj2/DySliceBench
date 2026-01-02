# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import product, accumulate, combinations, product
#import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 10 ** 9 + 7

def mapline(t = int):
    return map(t, sysread().split())
def mapread(t = int):
    return map(t, read().split())

def generate_inv(n,mod):
    """
    逆元行列
    n >= 2
    Note: mod must bwe a prime number
    """
    ret = [0, 1]
    for i in range(2,n+1):
        next = -ret[mod%i] * (mod // i)
        next %= mod
        ret.append(next)
    return ret

def run():
    N, *A = mapread()
    maxA = max(A)
    L = maxA.bit_length()
    subs = [0] * L
    for k in range(L):
        sum = 0
        for a in A:
            if (a >> k) & 1:
                sum += 1 << k
            sum %= mod
        subs[k] = sum

    sumA = 0
    for a in A:
        sumA += a
        sumA %= mod
    ret = 0
    ret += (sumA * N) % mod
    ret += (sumA * N) % mod

    sub_sum = 0
    for a in A:
        sums = 0
        for k in range(L):
            if (a >> k) & 1:
                sums += subs[k] * 2
                sums %= mod
        sub_sum += sums
        sub_sum %= mod

    ret -= sub_sum
    ret %= mod

    inv = generate_inv(2, mod)
    ret *= inv[2]
    ret %= mod
    print(ret)


if __name__ == "__main__":
    run()
