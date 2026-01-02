import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,sqrt
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

def numberlize(n):
    k="000000"
    u=6-len(str(n))
    return k[0:u]+str(n)
#print(numberize(5))
    
    
n,m=MI()
lis=[[]for i in range(n)]
for i in range(m):
    a,b=MI()
    lis[a-1].append([i+1,b])
#print(lis)
for j in range(n):
    lis[j]=sorted(lis[j],key=lambda x:x[1])
    for k in range(len(lis[j])):
        lis[j][k][1]=k+1
#print(lis)

ans=[0 for i in range(m)]
for j in range(n):
    for s in lis[j]:
        ans[s[0]-1]=[j+1,s[1]]
#print(ans)
for a in ans:
    print(numberlize(a[0])+numberlize(a[1]))