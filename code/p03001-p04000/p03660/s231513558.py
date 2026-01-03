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
from math import floor, ceil,pi,factorial,sqrt
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
    a,b=MI()
    a-=1
    b-=1
    tree[a].append(b)
    tree[b].append(a)
dis1=[-1 for i in range(n)]
dis2=[-1 for i in range(n)]
dis1[0]=0
dis2[-1]=0

def dfs1(x,l):
    for i in tree[x]:
        if dis1[i]>=0:
            continue
        else:
            dis1[i]=l+1
            dfs1(i,l+1)
dfs1(0,0)
#print(dis1)
def dfs2(x,l):
    for i in tree[x]:
        if dis2[i]>=0:
            continue
        else:
            dis2[i]=l+1
            dfs2(i,l+1)
dfs2(n-1,0)
#print(dis2)
count=0
for i in range(n):
    if dis1[i]<=dis2[i]:
        count+=1
    else:
        count-=1
if count<=0:
    print("Snuke")
else:
    print("Fennec")
    

        
        
        
            
        

                