import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
inf = 10**17
mod = 10**9 + 7
#s=input().rstrip()

n,m,q=MI()
strs=[[[] for i in range(m)] for i in range(n)]
for i in range(m):
    strs[0][i].append(str(i))
#print(strs)
for i in range(n-1):
    for j in range(m):
        for k in range(j,m):
            for s in strs[i][k]:
                strs[i+1][j].append(str(j)+s)
#print(strs)

L=strs[n-1]
#print(L)
lis=[]
for i in range(m):
    for s in L[i]:
        lis.append(s)
#print(lis)
mx=0
zyou=[LI() for i in range(q)]
for u in lis:
    po=0
    for k in range(q):
        a,b,c,d=zyou[k]
        if int(u[b-1])-int(u[a-1])==c:
            po+=d
    if po>mx:
        mx=po
print(mx)
