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
out=[(0,0,2,1),(1,0,2,1),(2,0,2,1),(3,0,2,1),(0,0,2,1),(0,1,2,1),(0,2,2,1),(0,3,2,1),(0,0,1,2),(1,0,1,2),(2,0,1,2),(3,0,1,2),(0,2,0,1),(1,2,0,1),(2,2,0,1),(3,2,0,1),(0,2,0,1),(0,2,1,1),(0,2,2,1),(0,2,3,1)]
dp=[[[[0]*4 for i in range(4)]for j in range(4)] for k in range(n-2)]
dp[0]=[[[1]*4 for i in range(4)] for j in range(4)]
dp[0][0][2][1]=0
dp[0][0][1][2]=0
dp[0][2][0][1]=0
for i in range(n-3):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                for m in range(4):
                    if (j,k,l,m) in out:
                        continue
                    else:
                        dp[i+1][k][l][m]+=dp[i][j][k][l]%mod
#print(dp)
ans=0
for i in range(4):
    for j in range(4):
        ans+=sum(dp[-1][i][j])%mod
print(ans%mod)