# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

N,Q=map(int,input().split())
a=tuple(map(int1,input().split()))
lr=[0]*Q
for i in range(Q):
    l,r=map(int1,input().split())
    lr[i]=(r<<40)+(l<<20)+i
lr.sort(reverse=1)
class BIT:
    def __init__(self,n):
        self.num=n
        self.dat=[0]*(self.num+1)
        self.depth=n.bit_length()
    
    def add(self,i,x):
        i+=1
        while i<=self.num:
            self.dat[i]+=x
            i+=i&-i
    
    def sum(self,i):
        i+=1
        s=0
        while i>0:
            s+=self.dat[i]
            i-=i&-i
        return s
    
    def lower_bound(self,x):
        sum_=0
        pos=0
        for i in range(self.depth,-1,-1):
            k=pos+(1<<i)
            if k<=self.num and sum_+self.dat[k]<x:
                sum_+=self.dat[k]
                pos+=1<<i
        return pos, sum_

b=BIT(N)
lastap=[-1]*N
ans=[-1]*Q
mask=(1<<20)-1
lr_pop=lr.pop
lrj=lr_pop()
j=lrj&mask
lrj>>=20
l=lrj&mask
r=lrj>>20
for i,x in enumerate(a):
    if lastap[x]!=-1:
        b.add(lastap[x],-1)
    b.add(i,1)
    lastap[x]=i
    while r==i:
        ans[j]=b.sum(r)-b.sum(l-1)
        if lr:            
            lrj=lr_pop()
            j=lrj&mask
            lrj>>=20
            l=lrj&mask
            r=lrj>>20
        else:
            l,r,j=-1,-1,-1
print(*ans,sep='\n')