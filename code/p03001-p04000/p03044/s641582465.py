# coding: utf-8
# hello worldと表示する
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
tree=[[] for i in range(n)]
for i in range(n-1):
    u,v,w=MI()
    u-=1
    v-=1
    tree[u].append([v,w])
    tree[v].append([u,w])
q=deque([[0,0]])
al=[-1 for i in range(n)]
#al[0]=0
col=[0 for i in range(n)]
def dfs(a,b):
    al[a]=0
    col[a]=b
    for x,y in tree[a]:
        if al[x]<0:
            dfs(x,(y+b)%2)
dfs(0,0)
#print(col)
for i in range(n):
    print(str(col[i]))

    
    
