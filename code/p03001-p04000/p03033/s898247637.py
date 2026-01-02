# coding: utf-8
import re
import math
import fractions
import random
from heapq import heappop,heappush
import time
import sys
input = sys.stdin.readline
#import numpy as np
mod=int(10**9+7)
inf=int(10**20)
class union_find():
    def __init__(self,n):
        self.n=n
        self.P=[a for a in range(N)]
        self.rank=[0]*n
 
    def find(self,x):
        if(x!=self.P[x]):self.P[x]=self.find(self.P[x])
        return self.P[x]
 
    def same(self,x,y):
        return self.find(x)==self.find(y)
 
    def link(self,x,y):
        if self.rank[x]<self.rank[y]:
            self.P[x]=y
        elif self.rank[y]<self.rank[x]:
            self.P[y]=x
        else:
            self.P[x]=y
            self.rank[y]+=1
 
    def unite(self,x,y):
        self.link(self.find(x),self.find(y))
 
    def size(self):
        S=set()
        for a in range(self.n):
            S.add(self.find(a))
        return len(S)
def bin_(num,size):
    A=[0]*size
    for a in range(size):
        if (num>>(size-a-1))&1==1:
            A[a]=1
        else:
            A[a]=0
    return A
def comb(n,r):return math.factorial(n)//math.factorial(n-r)//math.factorial(r)
def next_comb(num,size):
    x=num&(-num)
    y=num+x
    z=num&(~y)
    z//=x
    z=z>>1
    num=(y|z)
    if(num>=(1<<size)):return False
    else:
        return num
 

 
#main
N,Q=map(int,input().split())
E=[]
for a in range(N):
    s,t,x=map(int,input().split())
    E.append((s-x,1,x))
    E.append((t-x,0,x))

for a in range(Q):
    E.append((int(input()),2,0))
E.sort()
 
S=set()
H=[]
for time_,type_,x in E:
    if type_==1:
        S.add(x)
        heappush(H,x)
    elif type_==0:
        S.remove(x)
    else:
        while H and H[0] not in S:
            heappop(H)
        print(H[0] if H else -1)
