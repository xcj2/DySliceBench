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
lis=LI()
dp=[[0]*n for i in range(n)]
for i in range(n):
    if (n-1)%2==0:
        dp[i][i]=lis[i]
    else:
        dp[i][i]=-lis[i]
#print(dp)
for i in range(n-1,-1,-1):
    for j in range(n):
        #print(i,j)
        if i>=j:
            continue
        else:
            if (n-j+i-1)%2==0:
                if i+1>=n:
                    dp[i][j]=dp[i][j-1]+lis[j]
                elif j-1<0:
                    dp[i][j]=dp[i+1][j]+lis[i]
                else:
                    dp[i][j]=max(dp[i+1][j]+lis[i],dp[i][j-1]+lis[j])
            else:
                if i+1>=n:
                    dp[i][j]=dp[i][j-1]-lis[j]
                elif j-1<0:
                    dp[i][j]=dp[i+1][j]-lis[i]
                else:
                    dp[i][j]=min(dp[i+1][j]-lis[i],dp[i][j-1]-lis[j])
    #print(dp)
print(dp[0][-1])
        
            
