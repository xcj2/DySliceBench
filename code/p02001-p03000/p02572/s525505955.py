# coding: utf-8
#import numpy as np
import re
import math
from collections import defaultdict,deque,Counter
from fractions import Fraction
import bisect
import itertools
from itertools import accumulate
from copy import deepcopy

import heapq
import random
import time
import os
import sys
from functools import lru_cache,reduce
readline=sys.stdin.readline
sys.setrecursionlimit(100000)
alp="abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
mod=int(10**9+7)
inf=int(10**19)
class Set():
    def __init__(self,A=[]):
        self.heap=[]
        self.dic=defaultdict(bool)
        self.size=0
        for a in A:self.add(a)
    
    def __str__(self):
        return str(self.heap)
    
    def add(self,x):
        if not self.find(x):
            heapq.heappush(self.heap,x)
            self.dic[x]=True
            self.size+=1

    def remove(self,x):
        if self.find(x):
            self.dic[x]=False
            self.size-=1

    def find(self,x):
        return self.dic[x]
    
    def top(self):
        while self.heap and self.dic[self.heap[0]]==False:
            heapq.heappop(self.heap)
        if self.heap:return self.heap[0]
        else:return None

    def pop(self):
        ret=None
        if self.heap:
            ret=self.top()
            self.remove(ret)
        return ret
class multiset():
    def __init__(self,A=[]):
        self.heap=[]
        self.dic=defaultdict(int)
        self.size=0
        for a in A:self.add(a)
    
    def __str__(self):
        return str(self.heap)
    
    def add(self,x):
        heapq.heappush(self.heap,x)
        self.dic[x]+=1
        self.size+=1

    def remove(self,x):
        if self.dic[x]>0:
            self.dic[x]-=1
            self.size-=1
    
    def count(self,x):
        return self.dic[x]

    def find(self,x):
        return self.dic[x]>0
    
    def top(self):
        while self.heap and self.dic[self.heap[0]]==0:
            heapq.heappop(self.heap)
        if self.heap:return self.heap[0]
        else:return None

    def pop(self):
        ret=None
        if self.heap:
            ret=self.top()
            self.remove(ret)
        return ret
class Edge():
    def __init__(self,x,y,val=1):
        self.x=x
        self.y=y
        self.val=val
class Point():
    def __init__(self,y,x):
        self.x=x
        self.y=y
class unionfind():
    def __init__(self,n):
        self.n=n
        self.P=[a for a in range(n)]
        self.rank=[0]*n
 
    def find(self,x):
        if(x!=self.P[x]):
            self.P[x]=self.find(self.P[x])
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
def yn(b):print("yes" if b else "no")
def Yn(b):print("Yes" if b else "No")
def YN(b):print("YES" if b else "NO")
def ispow(a,b):
    now=b
    while now<a:
        now*=b
    return now==a
def getbin(num,size):
    A=[0]*size
    for a in range(size):
        if (num>>(size-a-1))&1==1:
            A[a]=1
        else:
            A[a]=0
    return A
def getfacs(n,mod_=0):
    A=[1]*(n+1)
    for a in range(2,len(A)):
        A[a]=A[a-1]*a
        if(mod_>0):A[a]%=mod_
    return A
def comb(n,r,mod,fac):
    if(n-r<0):return 0
    return (fac[n]*pow(fac[n-r],mod-2,mod)*pow(fac[r],mod-2,mod))%mod
def nextcomb(num,size):
    x=num&(-num)
    y=num+x
    z=num&(~y)
    z//=x
    z=z>>1
    num=(y|z)
    if(num>=(1<<size)):return False
    else:return num
def getprimes(n):
    if n==0:return []
    A=[True]*(n+1)
    A[0]=False
    A[1]=False
    for a in range(2,n+1):
        if A[a]:
            for b in range(a*2,n+1,a):
                A[b]=False
    ret=[]
    for a in range(n+1):
        if(A[a]):ret.append(a)
    return ret
def isprime(num):
    if(num<=1):return False
    i=2
    while i*i<=num:
       if(num%i==0):return False
       i+=1
    return True
def ifelse(b,t,f):return t if b else f
def factorize(n):
    b = 2
    ret=defaultdict(int)
    while b * b <= n:
        while n % b == 0:
            n //= b
            ret[b]+=1
        b+=1
    if n > 1:ret[n]+=1
    return ret
def inputintlist(row=1): 
    if row==1:
        ret=list(map(int,input().split()))
    else:
        ret=[None]*row
        for a in range(row):
            ret[a]=int(input())
    return ret
def inputfloatlist(row=1): 
    if row==1:
        ret=list(map(float,input().split()))
    else:
        ret=[None]*row
        for a in range(row):
            ret[a]=float(input())
    return ret
def istanchouzouka(A):
    f=True
    prev=min(A)-1
    for a in A:
        if prev>=a:
            f=False
        prev=a
    return f
def istanchouhigensyou(A):
    f=True
    prev=min(A)-1
    for a in A:
        if prev>a:
            f=False
        prev=a
    return f
def getallsum(A):
    s=sum(A)
    dp=defaultdict(int)
    dp[0]=1
    for a in range(0,len(A)):
        for b in range(s,-1,-1):
            if b-A[a]>=0:
                dp[b]+=dp[b-A[a]]
    return dp
def yuukoutomukou(edges):
    ret=deepcopy(edges)
    for edge in edges:
        if not edge.x==edge.y:
            ret.append(Edge(edge.y,edge.x,edge.val))
    return ret
def dijkstra(edges,V,start):
    from queue import PriorityQueue
    mincost=[inf]*V
    G=[[] for a in range(V)]
    for edge in edges:
        G[edge.x].append([edge.val,edge.y])
    Q=PriorityQueue()
    Q.put([0,start])#[cost,x]
    while not Q.empty():
        nowcost,nowx=Q.get()
        if mincost[nowx]==inf:
            mincost[nowx]=nowcost
            for cost,y in G[nowx]:
                newcost=nowcost+cost
                Q.put([newcost,y])
    return mincost
def warshallfloyd(edges,V):
    mincost=[[inf for b in range(V)] for a in range(V)]
    for a in range(V):mincost[a][a]=0
    for edge in edges:
        mincost[edge.x][edge.y]=min(mincost[edge.x][edge.y],edge.val)#x→yが複数ある場合のためにmin()する
    for k in range(V):
        for s in range(V):
            for t in range(V):
                if mincost[s][k]==inf or mincost[k][t]==inf:continue
                mincost[s][t]=min(mincost[s][t],mincost[s][k]+mincost[k][t])
    return mincost
def bellemanford(edges,V,start):
    mincost=[inf]*V
    mincost[start]=0
    for _ in range(V):
        for edge in edges:
            if mincost[edge.x]==inf:continue
            mincost[edge.y]=min(mincost[edge.y],mincost[edge.x]+edge.val)
    return mincost
def getmd(x1,y1,x2,y2):return abs(x1-x2)+abs(y1-y2)
def geted(x1,y1,x2,y2):return math.sqrt((x1-x2)**2+(y1-y2)**2)
class fordfulkerson():
    def __init__(self,edges,V,s,t):
        self.V=V
        self.used=[False]*V
        self.G=[[] for a in range(V)]
        self.s=s
        self.t=t
        for edge in edges:
            self.G[edge.x].append({"x":edge.x,"y":edge.y,"cap":edge.val,"rev":len(self.G[edge.y])})
            self.G[edge.y].append({"x":edge.y,"y":edge.x,"cap":0,"rev":len(self.G[edge.x])-1})
    def dfs(self,v,t,f=inf):
        if v==t:return f
        self.used[v]=True
        for a in range(len(self.G[v])):
            x=self.G[v][a]["x"]
            y=self.G[v][a]["y"]
            cap=self.G[v][a]["cap"]
            rev=self.G[y][self.G[x][a]["rev"]]
            if self.used[y] or cap==0:continue
            f2=self.dfs(y,t,min(f,cap))
            if f2>0:
                self.G[v][a]["cap"]-=f2
                rev["cap"]+=f2
                return f2
        return 0
    def maxflow(self):
        flow=0
        while True:
            self.used=[False]*V
            zouka=self.dfs(self.s,self.t)
            if zouka==0:break
            flow+=zouka
        return flow
def zipsort(*args):
    ziplist=sorted(zip(*args))
    for a in range(len(args)):
        for b in range(len(ziplist)):
            args[a][b]=ziplist[b][a]
def zipreverse(*args):
    ziplist=list(zip(*args))
    rev=[]
    for a in range(len(ziplist)-1,-1,-1):
        rev.append(ziplist[a])
    for a in range(len(args)):
        for b in range(len(rev)):
            args[a][b]=rev[b][a]

def to10(A):
    ret=0
    for a in range(len(A)-1,-1,-1):
        ret+=X[a]*2**(N-1-a)
    return ret
######################################################################################################
N=int(input())
A=inputintlist()
S=sum(A)
S%=mod
ans=0
for i in range(N):
    s=(S-A[i]+mod)%mod
    ans+=s*A[i]
    ans%=mod
ans=ans*pow(2,mod-2,mod)%mod
print(ans)

