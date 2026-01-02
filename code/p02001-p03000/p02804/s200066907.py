from collections import Counter,defaultdict,deque
import sys
import bisect
import math
import itertools
import string
import queue
import copy
# import numpy as np
# import scipy
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
 
def inp(): # n=1
    return int(input())
def inpm(): # x=1,y=2
    return map(int,input().split())
def inpl(): # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))
def inpls(): # a=['1','2','3',...,'n']
    return list(input().split())
def inplm(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return [list(map(int, input().split())) for _ in range(n)]

def extgcd(a,b): # ax+by=1 をみたす(x,y)の組を求める
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    return [w[0],w[1]]
# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return ( m + x%m ) % m
    
def nCk(n,k):
    res = 1
    a=n-k
    b=k
    for i in range(1,a+b+1):
        res = res*i%mod
    for i in range(1,a+1):
        res = res*mod_inv(i,mod)%mod
    for i in range(1,b+1):                                 
        res = res*mod_inv(i,mod)%mod
    return res
    
def main():
    n,k = inpm()
    z = inpl()
    z.sort()
    ans = 0

    res = 1
    a=n-k
    b=k-1
    for i in range(1,b+1):                                 
        res = res*mod_inv(i,mod)%mod
    for i in range(1,b+1):
        res = res*i%mod
    for i in range(1,a+2):
        ans = ( ans + z[k-2+i]*res)%mod
        ans = ( ans - z[n-k+1-i]*res)%mod
        res = res*(i+b)%mod
        res = res*mod_inv(i,mod)%mod
    print(ans)
    
if __name__ == "__main__":
    main()
