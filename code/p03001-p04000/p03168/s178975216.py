#BFSにdpを乗っける
#float型を許すな
#numpyはpythonで
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

n=I()
lis=list(map(float,input().rstrip().split(" ")))
dp=[[0]*(n+1) for i in range(n+1)]
dp[0][0]=1
for i in range(n):
    for j in range(n):
        dp[i+1][0]=dp[i][0]*(1-lis[i])
        dp[i+1][j+1]=dp[i][j]*lis[i]+dp[i][j+1]*(1-lis[i])
#print(dp)
ans=0
for i in range((n+1)//2,n+1):
    ans+=dp[-1][i]
print(ans)

            
    

        