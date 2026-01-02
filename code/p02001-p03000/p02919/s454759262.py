from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
import math
import time
import random
def I():
    return int(input())
def MI():
    return map(int,input().split())
def LI():
    return [int(i) for i in input().split()]
def LI_():
    return [int(i)-1 for i in input().split()]
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
ts=time.time()
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
show_flg=False
#show_flg=True

class Bit:
    def __init__(self,n):
        self.size=n
        self.m=len(bin(self.size))-2
        self.arr=[0]*(2**self.m+1)
        
    def __str__(self):
        return str(self.arr)
        
    def add(self,i,x):
        k=0
        while i<=self.size:
            k+=1
            self.arr[i]+=x
            i+=i&(-i)
        return
    
    def sum(self,i):
        rt=0
        while i>0:
            rt+=self.arr[i]
            i-=i&(-i)
        return rt
    
    def l_bound(self,w):
        if w<=0:
            return 0
        x=0
        k=2**self.m
        while k>0:
            if x+k<self.size and self.arr[x+k]<w:
                w-=self.arr[x+k]
                x+=k
            k//=2
        return x+1

        
class Bit0(Bit):
    def add(self,j,x):
        super().add(j+1,x)
    def l_bound(self,w):
        return max(super().l_bound(w)-1,0)

n=I()
a=LI()
p=[i+1 for i,j in sorted(enumerate(a),key=lambda x:x[1])]
bt=Bit0(n+2)
bt.add(0,1)
bt.add(n+1,1)
ans=0
for i in range(n-1,-1,-1):
    c=bt.sum(p[i])
    w,x,y,z=[bt.l_bound(c-1+i) for i in range(4)]
    c=p[i]
    bt.add(p[i],1)
    d=(i+1)*((x-w)*(y-c)+(c-x)*(z-y))
    ans+=d
print(ans)