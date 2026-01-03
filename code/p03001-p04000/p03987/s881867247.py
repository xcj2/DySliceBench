import bisect
import copy
import heapq
import math
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
sys.setrecursionlimit(500000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n=int(input())
a=list(map(int,input().split()))

dic={}
for i in range(n):
    dic[a[i]]=i+1

# Binary Indexed Tree (Fenwick Tree)
class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s
    def add(self, i, x):
        # assert i > 0
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i)

bi=BIT(n)
ans=0
# print(dic)
for i in range(n):
    lsum=bi.sum(dic[i+1])
    l,r=-1,dic[i+1]
    while r-l>1:
        half=(r+l)//2
        if bi.sum(half)>=lsum:
            r=half
        else:
            l=half
    ll=r
    rsum=bi.get(dic[i+1],n)
    l,r=dic[i+1],n+1
    while r-l>1:
        half=(r+l)//2
        if bi.get(half,n)>=rsum:
            l=half
        else:
            r=half
    rr=l
    ans+=(i+1)*(dic[i+1]-ll)*(rr-dic[i+1]+1)
    # print(ll,dic[i+1],rr)
    bi.add(dic[i+1],i+1)
    # print(ans)
    # print(bi.el)
print(ans)