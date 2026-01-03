from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
#import math
#import time
#import random  # randome is not available at Codeforces
def I():
    return int(input())
def MI():
    return map(int,input().split())
def LI():
    return [int(i) for i in input().split()]
def LI_():
    return [int(i)-1 for i in input().split()]
def StoI():
    return [ord(i)-97 for i in input()]
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
inf=float('inf')
#ts=time.time()
#sys.setrecursionlimit(10**6)
input=lambda: sys.stdin.readline().rstrip()

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

n,k=LI()
a=[0]
for _ in range(n):
    a.append(a[-1]+I()-k)

ans=0
show(a)
b=[(j,i) for i,j in enumerate(sorted(a[:]))]
d=dict(b)
b=[d[i] for i in a[:]]
show(b)

bt=Bit0(n+1)
for i in b:
    ans+=bt.sum(i+1)
    bt.add(i,1)

print(ans)


