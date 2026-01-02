import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
# from collections import Counter,defaultdict,deque
# from itertools import permutations, combinations
# from heapq import heappop, heappush
# from fractions import gcd
import functools
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])
def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)
k = inp()
ans = 0
for a in range(1,k+1):
    for b in range(1,k+1):
        for c in range(1,k+1):
            ans += functools.reduce(euclid,[a,b,c])

print(ans)