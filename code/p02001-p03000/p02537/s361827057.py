ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
import sys

class SegmentTree():
    def __init__(self,n):
        self.e = 0
        self.r = 0 #ノードの段数
        cnt = 0
        while cnt<n:
            cnt=2**self.r
            self.r +=1
        self.tree = [self.e]*(2**self.r -1)# 0-index
        self.n = 2**(self.r-1) #一番下のnodeの数
    def build(self,lis):
        for i,val in enumerate(lis):
            self.update(i,val)
    def func(self,a,b): #適宜書き換え
        return max(a,b)
    def update(self,i,val):
        i += self.n -1
        self.tree[i] =self.func(self.tree[i],val)
        while i>0:
            i = (i-1)//2
            self.tree[i] = self.func(self.tree[i*2+1],self.tree[i*2+2])
    def query(self,l,r):
        l += self.n -1
        r += self.n -1 #半開区間[l,r) ==[l,r-1]  に対するquery
        lval = self.e
        rval = self.e
        while r>l:
            if l%2 == 0:
                lval = self.func(lval,self.tree[l])
                l+=1
            if r%2==0:
                rval = self.func(rval,self.tree[r-1])
                r-=1
            r//=2
            l//=2
        return self.func(lval,rval)
    def index(self,i):
        return i+self.n -1
    def value(self,i):
        return self.tree[i+self.n -1]

n,k = ma()
LR = []
A=[]
for i in range(n):
    A.append(ni())

mx=max(A)
dp = SegmentTree(mx+1)
for a in A:
    max_len = dp.query(max(0,a-k),min(mx+1,a+k+1))
    dp.update(a,max_len+1)
print(dp.query(0,mx+1))
