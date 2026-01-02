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

n,m,que=MI()
lis=[[0]*n for i in range(n)]
for i in range(m):
    l,r=MI()
    lis[l-1][r-1]+=1
for i in range(n):
    lis[i]=list(accumulate(lis[i]))
#print(lis)
for i in range(que):
    p,q=MI()
    ans=0
    for i in range(p,q+1):
        if i==1:
            ans+=lis[i-1][q-1]
        else:
            ans+=lis[i-1][q-1]-lis[i-1][i-2]
    print(ans)