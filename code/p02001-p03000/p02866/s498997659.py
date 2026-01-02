from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
#import math
#import time
import random  # randome is not available at Codeforces
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
#eps=10**(-10)
#ts=time.time()
#sys.setrecursionlimit(10**6)
input=lambda: sys.stdin.readline().rstrip()

show_flg=False
#show_flg=True


mo=998244353

n=I()
d=LI()
dp=[0]*(1+n)
ans=1
if d[0]!=0:
    ans=0
if d.count(0)!=1:
    ans=0
m=0

for i in d:
    dp[i]+=1
    m=max(i,m)

for i in range(m):
    pt=pow(dp[i],dp[i+1],mo)
    ans*=pt
    ans%=mo


print(ans%mo)
