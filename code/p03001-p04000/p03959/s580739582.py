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

 
def main():
    n = inp()
    t = inpl()
    a = inpl()
    m = [0 for _ in range(n)]
    m[0] = t[0]
    for i in range(1,n):
        if t[i]>t[i-1]:
            m[i] = t[i]
    m[n-1] = a[n-1]
    for i in range(n-2,-1,-1):
        if a[i]>a[i+1]:
            m[i] = a[i]
    ans = 1
    mt,ma = 0,0
    for i in range(n):
        mt = max(mt,m[i])
        ma = max(ma,m[n-1-i])
        if mt != t[i] or ma != a[n-1-i]:
            print(0)
            return
    for i in range(n):
        if m[i] == 0:
            ans = (ans*min(t[i],a[i]))%mod
    print(ans)
    
if __name__ == "__main__":
    main()