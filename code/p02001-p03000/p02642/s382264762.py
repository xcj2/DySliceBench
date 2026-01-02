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
lis=LI()
c=Counter(lis)
lis=list(set(lis))
m=10**6+1
dp=[0 for i in range(m)]
#print(dp)
for i in range(len(lis)):
    x=lis[i]
    #print(x)
    for j in range(2,((m-1)//x)+1):
        dp[x*j]=1
        #print(x*j)
#print(5*j)
#print(dp)
ans=0
#print(dp[10**6])
for y in lis:
    if c[y]<=1:
        ans+=1-dp[y]
print(ans)
#print(dp)
#print(dp[2*(10**5)])
