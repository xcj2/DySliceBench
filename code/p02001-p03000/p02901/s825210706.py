from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
#import math
#import time
import random
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
#ts=time.time()
sys.setrecursionlimit(10**6)
#input=sys.stdin.readline
show_flg=False
#show_flg=True

n,m=MI()
t=1<<n
key=[]
for i in range(m):
    a,b=MI()
    c=0
    for j in LI_():
        c+=1<<j
    key.append((a,c))
inf=float('inf')
dp=[[inf]*(m+1) for _ in range(t)]
#dp[stat][m] # min value using up to m and open stat
dp[0][0]=0

for j in range(1,m+1):
    for i in range(t):
        cost,ck=key[j-1]
        show(i,j,'|',dp[ck|i][j],min(dp[ck|i][j-1],dp[i][j-1]+cost))
        dp[ck|i][j]=min(dp[ck|i][j],dp[ck|i][j-1],dp[i][j-1]+cost)
        dp[i][j]=min(dp[i][j],dp[i][j-1])
        
for i in dp:
    show(*i)

ans=dp[t-1][m] if dp[t-1][m]!=inf else -1
print(ans)
