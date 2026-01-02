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

n,k=MI()
factmod=[1 for i in range(n+1)]
for i in range(n):
    factmod[i+1]=(factmod[i]*(i+1))%mod
#print(factmod)
ans=0
for m in range(min(k+1,n)):
    a=factmod[-1]*pow((factmod[m]*factmod[n-m])%mod,mod-2,mod)
    b=factmod[n-1]*pow((factmod[m]*factmod[n-m-1])%mod,mod-2,mod)
    ans=(ans+(a*b))%mod
print(ans%mod)

    
