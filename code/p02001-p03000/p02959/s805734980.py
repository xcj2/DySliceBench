import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
# from collections import Counter,defaultdict,deque
# from itertools import permutations, combinations
# from heapq import heappop, heappush
# # input = sys.stdin.readline
# sys.setrecursionlimit(10**8)
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

n = inp()
al = inpl()
bl = inpl()
ans = 0
rem = 0
for i in range(0, n):
    if(al[i] <= bl[i] + rem):
        tmp = al[i] - rem
        if(tmp <= 0):
            tmp = 0
        rem = bl[i] - tmp
        ans += al[i]
    else:
        ans += bl[i] + rem
        rem = 0
if(al[n] >= rem):
    ans += rem
else:
    ans += al[n]
print(ans)
    
