# coding: utf-8
import re
import math
import itertools
from copy import deepcopy
import fractions
import random
from functools import lru_cache
from heapq import heappop,heappush
import time
import sys
readline = sys.stdin.readline
sys.setrecursionlimit(2000)
#import numpy as np
alphabet="abcdefghijklmnopqrstuvwxyz"
mod=int(10**9+7)
inf=int(10**20)
def yn(b):
    if b:
        print("yes")
    else:
        print("no")
def Yn(b):
    if b:
        print("Yes")
    else:
        print("No")
def YN(b):
    if b:
        print("YES")
    else:
        print("NO")
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
def get_primes(n,type="int"):
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
def join(A,c=" "):
    n=len(A)
    A=list(map(str,A))
    s=""
    for a in range(n):
        s+=A[a]
        if(a<n-1):s+=c
    return s
#main

@lru_cache(maxsize=None)#メモ化デコレータ
def f(num,k):
    if(num==0 and k==0):return 1
    elif(num<=0 or k<0):return 0
    else:
        r=num-(num//10)*10
        m=num//10
        return f(m,k-1)*r+f(m-1,k-1)*(9-r)+f(m,k)
s=int(input())
k=int(input())
print(f(s,k))
