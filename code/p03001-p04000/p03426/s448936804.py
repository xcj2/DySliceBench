import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
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

def main():
    h,w,d = inpm()
    a = inpll(h)
    MAP = [0 for _ in range(h*w)]
    for i in range(h):
        for j in range(w):
            MAP[a[i][j]-1] = (i,j)
    cnt = []
    for i in range(h*w-d):
        x = MAP[i]
        y = MAP[i+d]
        cost = abs(x[0]-y[0]) + abs(x[1]-y[1])
        cnt.append(cost)
    ans = [0 for _ in range(h*w)]
    for i in range(h*w-d):
        ans[i+d] += ans[i] + cnt[i]
    q = inp()
    for _ in range(q):
        l,r = inpm()
        print(ans[r-1]-ans[l-1])
 
if __name__ == "__main__":
    main()