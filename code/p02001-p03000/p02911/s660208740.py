import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
# from collections import Counter,defaultdict,deque
# from itertools import permutations, combinations
# from heapq import heappop, heappush
# # input = sys.stdin.readline
# sys.setrecursionlimit(10**8)
# mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

n, k , q = inpm()
al = inplm(q)
l = []
for i in range(0, n):
    l.append(k)
for i in range(0, q):
    l[al[i] - 1] += 1
for i in range(0, n):
    print('Yes' if l[i] - q > 0 else 'No')
