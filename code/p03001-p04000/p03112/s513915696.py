import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input()) # n=1
def inpm(): return map(int,input().split()) # x=1,y=2
def inpl(): return list(map(int, input().split())) # a=[1,2,3,4,5,...,n]
def inpls(): return list(input().split())  # a=['1','2','3',...,'n']
def inplm(n): return list(int(input()) for _ in range(n)) # x=[] 複数行
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)] # [[2,2,2,2],[1,1,1,1],[3,3,3,3]] 
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)]) # [[1,1,1,1],[2,2,2,2],[3,3,3,3]] 
def graph():
    n=inp()
    g=[[] for _ in range(n)]
    for i in range(n):
        a = inp()
        a -= 1
        g[i].append(a)
        g[a].append(i)
    return n,g

def f(li, x):
    n = len(li)
    ok = -1
    ng = n
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if li[mid] < x:
            ok = mid
        else:
            ng = mid
    return ok

def main():
    a,b,q = inpm()
    s = inplm(a)
    t = inplm(b)
    x = inplm(q)
    s = tuple(s)
    t = tuple(t)
    x = tuple(x)
    for i in range(q):
        start = x[i]
        n = len(s)
        ok = -1
        ng = n
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if s[mid] < start:
                ok = mid
            else:
                ng = mid
        index_s = ok
        n = len(t)
        ok = -1
        ng = n
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if t[mid] < start:
                ok = mid
            else:
                ng = mid
        index_t = ok
        a1 = 10**11
        b1 = 10**11
        c1 = 10**11
        d1 = 10**11
        if index_t+1 < b and index_s+1 < a:
            d1 = abs(max(s[index_s+1],t[index_t+1]) - start)
        if index_s >= 0 and index_t+1 < b:
            a1 = min(abs(start - s[index_s]) + abs(s[index_s] - t[index_t+1]), abs(start - t[index_t+1]) + abs(s[index_s] - t[index_t+1]) )  
        if index_t >= 0 and index_s+1 < a:
            b1 = min(abs(start - t[index_t]) + abs(s[index_s+1] - t[index_t]),abs(start - s[index_s+1]) + abs(s[index_s+1] - t[index_t]))
        if index_s >= 0 and index_t >= 0:
            c1 = abs(start - min(s[index_s],t[index_t]))
        print(min(a1,b1,c1,d1))

if __name__ == "__main__":
    main()