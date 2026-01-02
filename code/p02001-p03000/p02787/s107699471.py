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
def inpll(n): return sorted([list(map(int, input().split())) for _ in range(n)]) # [[1,1,1,1],[2,2,2,2],[3,3,3,3]] 
def graph():
    n=inp()
    g=[[] for _ in range(n)]
    for i in range(n):
        a = inp()
        a -= 1
        g[i].append(a)
        g[a].append(i)
    return n,g

def Knapsack2(W,w,v,h): # n個の品物(重さw[i],価値v[i]) 価値iを達成する重量の最小化 計算量O(V*N)
    n=len(w)
    v_max=max(v)+h+5
    # dp[i] : 価値iの組み合わせを達成する重量の最小値
    dp=[0]+[float('inf') for _ in range(v_max+1)]
    for i in range(n):
        for j in range(0,v_max+1):
            if j >= v[i]:
                if j-v[i]>W:
                    continue
                dp[j]=min(dp[j],dp[j-v[i]]+w[i])
    ans = 10**10
    for i in range(h,v_max+1):
        ans = min(ans,dp[i])
        
    print(ans)

def main():
    h,n = inpm()
    a = []
    b = []
    for _ in range(n):
        a1,b1 = inpm()
        a.append(a1)
        b.append(b1)
    Knapsack2(h,b,a,h)

    
if __name__ == "__main__":
    main()


