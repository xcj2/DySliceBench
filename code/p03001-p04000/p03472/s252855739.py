import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7
#s=input().rstrip()

n,h=MI()
A=[]
B=[]
for i in range(n):
    a,b=MI()
    A.append(a)
    B.append(b)
#print(B)
A.sort(reverse=True)
B.sort(reverse=True)
ace=A[0]
throw=[]
for b in B:
    if b>ace:
        throw.append(b)
if h>sum(throw):
    slash1=ceil((h-sum(throw))/ace)
    h-=ace*slash1
    ans=slash1+len(throw)
else:
    for i in range(len(throw)):
        h-=throw[i]
        if h<=0:
            ans=i+1
            break
print(ans)