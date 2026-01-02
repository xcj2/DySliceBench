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
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n=int(input())
p=list(map(int,input().split()))

dic={}
for i in range(n):
    dic[p[i]]=i
# print(dic)

# Binary Indexed Tree (Fenwick Tree)
class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)
    # [1,i]の足し算
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
    # [i,j]の足し算
    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i-1)

bi=BIT(n+1)
ans=0
for i in range(n)[::-1]:
    bi.add(dic[i+1]+1,i+1)
    # print(bi.el)
    lsum=bi.get(1,dic[i+1])
    l,r=-1,dic[i+1]
    while r-l>1:
        half=(r+l)//2
        if bi.get(1,half)>=lsum:
            r=half
        else:
            l=half
    l1=r
    l2=-1
    if r!=0:
        lsum=bi.get(1,r-1)
        l,r=-1,r-1
        while r-l>1:
            half=(r+l)//2
            if bi.get(1,half)>=lsum:
                r=half
            else:
                l=half
        l2=r
    # print(l1,l2)
    rsum=bi.get(dic[i+1]+2,n)
    l,r=dic[i+1]+2,n+2
    while r-l>1:
        half=(r+l)//2
        if bi.get(half,n)>=rsum:
            l=half
        else:
            r=half
    # print(rsum,l,r)
    r1=l
    r2=n+1
    if r!=n+1:
        rsum=bi.get(r1+1,n)
        l,r=r1+1,n+2
        while r-l>1:
            half=(r+l)//2
            if bi.get(half,n)>=rsum:
                l=half
            else:
                r=half
        r2=l
    # print(l2,l1)
    # print(r1,r2)
    # print(bi.el)
    if i==n-1:
        continue
    if l1+l2==-1:
        ans+=(dic[i+1]+1-l1)*(r2-r1)*(i+1)
    elif r1+r2==2*n+3:
        ans+=(l1-l2)*(r1-dic[i+1]-1)*(i+1)
    elif l2+4==r2:
        ans+=2*(i+1)
    else:
        ans+=((l1-l2)*(r1-dic[i+1]-1)+(dic[i+1]+1-l1)*(r2-r1))*(i+1)
    # print(l1-l2,r1-dic[i+1]-1,dic[i+1]+1-l1,r2-r1)
    # print(ans)
print(ans)