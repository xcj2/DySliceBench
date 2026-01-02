'''
    Auther: ghoshashis545 Ashis Ghosh
    College: jalpaiguri Govt Enggineerin College

'''
import sys
from collections import deque,defaultdict as dd 
from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
from itertools import permutations
from datetime import datetime
from math import ceil,sqrt,log,gcd
def ii():return int(input())
def si():return input()
def mi():return map(int,input().split())
def li():return list(mi())
abc='abcdefghijklmnopqrstuvwxyz'
abd={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
mod=1000000007
#mod=998244353
inf = float("inf")
vow=['a','e','i','o','u']
dx,dy=[-1,1,0,0],[0,0,1,-1]



def solve():
    
    
    
    # for _ in range(ii()):
    
    
    n,m = mi()
    
    par = [i for i in range(n+1)]
    sz = [1]*(n+1)
    
    def find(i):
        if i == par[i]:
            return par[i]
        par[i] = find(par[i])
        return par[i]
    
    def union(u,v):
        u = find(u)
        v = find(v)
        if u!= v:
            if sz[u]>sz[v]:
                par[v] = u
                sz[u]+=sz[v]
            else:
                par[u] = v
                sz[v] += sz[u]
    
    
    for i in range(m):
        x,y = mi()
        union(x,y)
    print(max(sz))
    
    
if __name__ =="__main__":
    # read()
    solve()
    