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
dp=[[-1]*n for i in range(n)]
acc=list(accumulate(lis))
for i in range(n):
    dp[i][i]=0
def memo(x,y):
    if dp[x][y]>=0:
        return dp[x][y]
    res=inf
    for i in range(x,y):#左側区間の右端
        if x==0:
            if acc[y]+memo(x,i)+memo(i+1,y)<res:
                res=acc[y]+memo(x,i)+memo(i+1,y)
        else:
            if acc[y]-acc[x-1]+memo(x,i)+memo(i+1,y)<res:
                res=acc[y]-acc[x-1]+memo(x,i)+memo(i+1,y)
    dp[x][y]=res
    return res
        
for i in range(n):
    for j in range(i,n):
        memo(i,j)
#print(dp)
print(dp[0][-1])

        

        
    
