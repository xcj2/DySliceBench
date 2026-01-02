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
show_flg=True

n,m=LI()

#####min######
#def min(x,y):
#    return 

def init(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]    
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=min(seg[2*i+1],seg[2*i+2]) 

def update(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = min(seg[k*2+1],seg[k*2+2])
    
def query(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = min(res,seg[p])
        if q&1 == 1:
            res = min(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = min(res,seg[p])
    else:
        res = min(min(res,seg[p]),seg[q])
    return res

#####単位元######
ide_ele = inf

ans=inf

s=[int(i) for i in input()]

def dp(b,m): # N log (N)
    N=len(b)-1
    n=N+1
    global seg
    global num
    
    #num:n以上の最小の2のべき乗
    num =2**(n-1).bit_length()
    seg=[ide_ele]*2*num
    init([inf]*n)
    
    update(0,0)

    dp=[0]+[inf]*(N)
    for i in range(N):
        if b[i+1]==1:
            continue
        dp[i+1]=query(max(i-m+1,0),i+1)+1
        update(i+1,dp[i+1])
        #show(seg)
        #show(dp)
    return dp

dp1=dp(s,m)
step=dp1[n]
if step==inf:
    print(-1)
    exit()

dp2=dp(s[::-1],m)[::-1]

move=[0]
ans=[]
j=1
for i in range(step,0,-1): # N
    while j<=n and dp2[j]!=i-1:
        j+=1
    #ans.append(j-move[-1])
    move.append(j)

# 2 * N log N + N
'''
show(s)
show(dp1,step)
show(dp2)
show(move)
'''

for i in range(len(move)-1):
    ans.append(move[i+1]-move[i])
print(*ans)

