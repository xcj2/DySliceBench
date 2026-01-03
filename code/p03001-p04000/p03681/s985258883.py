#dpでできないかな？
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

'''def factmod(n):
    u=1
    for i in range(1,n+1):
        u=u*i%mod
    return u'''
factmod=[0 for i in range(100000)]
factmod[0]=1
for i in range(100000-1):
    factmod[i+1]=factmod[i]*(i+2)%mod
#print(factmod)
        
n,m=MI()
if n>m+1 or m>n+1:
    print(0)
    sys.exit()
elif n==m:
    ans=2*factmod[n-1]**2
else:
    if m>n:
        m,n=n,m
    ans=factmod[n-1]*factmod[m-1]
print(ans%mod)