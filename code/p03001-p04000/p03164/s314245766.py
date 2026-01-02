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

n,w=MI()
WV=[LI() for i in range(n)]
dp=[[inf]*(10**5+1) for i in range(n+1)]
dp[0][0]=0
for i in range(n):
    for j in range(10**5+1):
        if j-WV[i][1]>=0:
            dp[i+1][j]=min(dp[i+1][j],dp[i][j],dp[i][j-WV[i][1]]+WV[i][0])
        else:
            dp[i+1][j]=min(dp[i+1][j],dp[i][j])
for i in range(10**5+1):
    j=10**5-i
    if dp[-1][j]<=w:
        print(j)
        sys.exit()




            

    
    

