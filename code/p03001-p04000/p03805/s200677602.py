# coding: utf-8
# hello worldと表示する
import sys
import numpy
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
from operator import itemgetter
from copy import deepcopy
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

n,m=MI()
tree=[[] for i in range(n)]
for i in range(m):
    a,b=MI()
    a-=1;b-=1
    tree[a].append(b)
    tree[b].append(a)
#print(tree)
#count=0
#global count
count=0
def dfs(x,al):
    global count
    if len(al+[x])==n:
        count+=1
        #print(count)
        return
    #if x==0:
        #al=[]
    #al.append(x)
    #print(al)
    for y in tree[x]:
        if not (y in al):
            #print(y,al+[x])
            dfs(y,al+[x]) #return
dfs(0,[])
print(count)