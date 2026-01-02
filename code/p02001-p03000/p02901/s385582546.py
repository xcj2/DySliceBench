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


n,m=MI()
data=[]
for i in range(m):
    a,b=MI()
    c=LI()
    u=0
    for x in c:
        u+=2**(x-1)
    data.append([a,u])
data.sort()
#print(data)
dp=[[inf]*(2**n) for i in range(m+1)]
dp[0]=[inf]*(2**n)
dp[0][0]=0
#print(dp)
for i in range(m):
    for j in range(2**n):
        dp[i+1][j|data[i][1]]=min(dp[i+1][j|data[i][1]],dp[i][j|data[i][1]],dp[i][j]+data[i][0])
        dp[i+1][j]=min(dp[i][j],dp[i+1][j])
        #print(i+1,j|data[i][1],dp[i][j|data[i][1]],dp[i][j]+data[i][0])
    #print()
#print(dp)
if dp[-1][-1]>=inf:
    print(-1)
else:
    print(dp[-1][-1])