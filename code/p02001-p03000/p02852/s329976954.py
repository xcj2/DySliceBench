from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
import math
import time
#import random
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
def ItoS(nn):
    return chr(nn+97)
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
inf=float('inf')
l_alp=string.ascii_lowercase
u_alp=string.ascii_uppercase
ts=time.time()
#sys.setrecursionlimit(10**6)
input=lambda: sys.stdin.readline().rstrip()

show_flg=False
#show_flg=True

n,m=LI()

## Segment Tree ##

## Initializer Template ##
# Range Sum:        sg=SegTree(n,0)
# Range Minimum:    sg=SegTree(n,inf,min,inf)

class SegTree:

    def __init__(self,n,init_val=0,function=lambda a,b:a+b,ide=0):
        self.n=n
        self.ide_ele=ide_ele=ide
        self.num=num=2**(n-1).bit_length()
        self.seg=seg=[self.ide_ele]*2*self.num
        self.segfun=segfun=function
        #set_val
        for i in range(n):
            self.seg[i+self.num-1]=init_val
        #built
        for i in range(self.num-2,-1,-1) :
            self.seg[i]=self.segfun(self.seg[2*i+1],self.seg[2*i+2]) 
    
    def update(self,k,x):
        k += self.num-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfun(self.seg[k*2+1],self.seg[k*2+2])
        
    def query(self,p,q):
        if q<=p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res=self.ide_ele
        while q-p>1:
            if p&1 == 0:
                res = self.segfun(res,self.seg[p])
            if q&1 == 1:
                res = self.segfun(res,self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.segfun(res,self.seg[p])
        else:
            res = self.segfun(self.segfun(res,self.seg[p]),self.seg[q])
        return res

    def __str__(self):
        # 生配列を表示
        rt=self.seg[self.num-1:self.num-1+self.n]
        return str(rt)

s=[int(i) for i in input()]

def dp(b,m): # N log (N)
    N=len(b)-1
    n=N+1
    sg=SegTree(n,inf,min,inf)

    sg.update(0,0)

    dp=[0]+[inf]*(N)
    for i in range(N):
        if b[i+1]==1:
            continue
        dp[i+1]=sg.query(max(i-m+1,0),i+1)+1
        sg.update(i+1,dp[i+1])
        #show(seg)
    
    show(sg)

    return dp

dp1=dp(s,m)
step=dp1[n]
if step==inf:
    print(-1)
    exit()

dp2=dp(s[::-1],m)[::-1]

show(dp1,'dp1')
move=[0]
ans=[]
j=1
for i in range(step,0,-1): # N
    while j<=n and dp2[j]!=i-1:
        j+=1
    move.append(j)

for i in range(len(move)-1):
    ans.append(move[i+1]-move[i])
print(*ans)
