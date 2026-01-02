# coding: utf-8
import re
import math
from copy import deepcopy
import fractions
import random
from heapq import heappop,heappush
import time
import sys
readline = sys.stdin.readline
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
def fac_list(n,mod_=0):
    A=[1]*(n+1)
    for a in range(2,len(A)):
        A[a]=A[a-1]*a
        if(mod>0):A[a]%=mod_
    return A
def comb(n,r,mod,fac):
    if(n-r<0):return 0
    return (fac[n]*pow(fac[n-r],mod-2,mod)*pow(fac[r],mod-2,mod))%mod
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
def get_primes(n,type="number"):
    A=[True]*(n+1)
    A[0]=False
    A[1]=False
    for a in range(2,n+1):
        if A[a]:
            for b in range(a*2,n+1,a):
                A[b]=False
    if(type=="bool"):return A
    B=[]
    for a in range(n+1):
        if(A[a]):B.append(a)
    return B
def is_prime(num):
    if(num<=2):return False
    i=2
    while i*i<=num:
       if(num%i==0):return False
       i+=1
    return True

fac=fac_list(10**5+100,mod)
def C(n,r):
    if(n-r<0):return 0
    return (fac[n]*pow(fac[n-r],mod-2,mod)*pow(fac[r],mod-2,mod))%mod

 
#main
N,K=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
ans=0
if(K>=2):
    for a in range(0,N):
        ans+=C(a,K-1)*(A[a])
        ans%=mod
    for a in range(0,N):
        len=N-1-a
        ans-=C(len,K-1)*(A[a])
        ans%=mod
print(ans)

