# -*- coding: utf-8 -*-
import sys
# from collections import defaultdict, deque
from math import log10, sqrt, ceil
def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline()[:-1]

def c(x):
    cnt = 0
    n = x
    while n:
        n //= 10
        cnt += 1
    return cnt

def solve():
    n = int(input())
    o = n
    ans = c(n)
    for i in range(2, int(sqrt(n)) + 3):
        if (n % i == 0):
            a = i
            b = o // a
            ans = min(ans, max(c(a), c(b)))
        if i > n:
            break

    print(ans)
    
        




t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()



"""
1 -> (1, 2) -> (2 ** 3, 3) -> (3, 1)
100000007
"""

