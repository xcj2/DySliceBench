#dpでできないかな？
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
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

n=I()
tree=[[] for i in range(n)]
for i in range(n-1):
    a,b,c=MI()
    a-=1
    b-=1
    tree[a].append([b,c])
    tree[b].append([a,c])
q,k=MI()
#print(tree)
k-=1
dis=[[-1,0] for i in range(n)]
dis[k][0]=0
def dfs(x):
    for s,t in tree[x]:
        if dis[s][0]>=0:
            continue
        dis[s][0]=dis[x][0]+t
        if x==k:
            dis[s][1]=s
        else:
            dis[s][1]=x
        dfs(s)
dfs(k)
for i in range(q):
    x,y=MI()
    x-=1
    y-=1
    print(dis[x][0]+dis[y][0])