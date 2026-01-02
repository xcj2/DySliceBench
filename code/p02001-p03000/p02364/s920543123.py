#import pysnooper
#import numpy
#import os,re,sys,operator
#from collections import Counter,deque
from operator import itemgetter
#from itertools import accumulate,combinations,groupby,combinations_with_replacement,permutations
from sys import stdin,setrecursionlimit
#from bisect import bisect_left
#from copy import deepcopy
#import heapq
#import math
#import string
#from time import time

setrecursionlimit(10**6)
input=stdin.readline

class Union_find:
    
    def __init__(self,n):
        self.n=n
        self.root=[-1]*(n+1)
        self.rank=[0]*(n+1)
    
    def find_root(self,x):
    
        if self.root[x]<0: return x
        else:
            self.root[x]=self.find_root(self.root[x])
            return self.root[x]
    
    def unite(self,x,y):
    
        x,y=self.find_root(x),self.find_root(y)
    
        if x==y: return 
        elif self.rank[x]>self.rank[y]:
            self.root[x]+=self.root[y]
            self.root[y]=x
        else:
            self.root[y]+=self.root[x]
            self.root[x]=y
            if self.rank[x]==self.rank[y]: self.rank[y]+=1
    
    def same(self,x,y):
        return self.find_root(x)==self.find_root(y)
    
    def count(self,x):
        return -self.root[self.find_root(x)]

v,e=map(int,input().split())
graph=Union_find(v)

a=sorted([list(map(int,input().split())) for _ in range(e)],key=itemgetter(2))
ans=0
for i in a:
    s,t,w=i
    if not graph.same(s,t):
        graph.unite(s,t)
        ans+=w
print(ans)
