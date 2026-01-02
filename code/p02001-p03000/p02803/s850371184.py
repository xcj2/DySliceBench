
def s0():return input()
def s1():return input().split()
def s2(n):return [input() for x in range(n)]
def s3(n):return [input().split() for _ in range(n)]
def s4(n):return [[x for x in s] for s in s2(n)]
def n0():return int(input())
def n1():return [int(x) for x in input().split()]
def n2(n):return [int(input()) for _ in range(n)]
def n3(n):return [[int(x) for x in input().split()] for _ in range(n)]
def t3(n):return [tuple(int(x) for x in input().split()) for _ in range(n)]
def p0(b,yes="Yes",no="No"): print(yes if b else no)
# from sys import setrecursionlimit
# setrecursionlimit(1000000)
from collections import Counter,deque,defaultdict
import itertools
# import math
# import networkx as nx
# from bisect import bisect_left,bisect_right
# from heapq import heapify,heappush,heappop

h,w=n1()
s=s4(h)
def make_around(s):
    sss=[[-1]*(w+2)]
    for line in s:
        sss.append([-1]+[-1 if i=="#" else 0 for i in line ]+[-1])
    sss.append([-1]*(w+2))
    return sss

s=make_around(s)
d=[]
for i in range(1,h+1):
    for j in range(1,w+1):
        if s[i][j]==0:
            d.append((i,j))

from copy import deepcopy
ans=0
for i in range(len(d)):
    ss=deepcopy(s)
    x,y=d[i]
    q=deque([(x,y)])
    ss[x][y]=1
    while len(q)>0:
        x,y=q.popleft()
        if ss[x+1][y]==0:
            ss[x+1][y]=ss[x][y]+1
            q.append((x+1,y))
        if ss[x-1][y]==0:
            ss[x-1][y]=ss[x][y]+1
            q.append((x-1,y))
        if ss[x][y+1]==0:
            ss[x][y+1]=ss[x][y]+1
            q.append((x,y+1))
        if ss[x][y-1]==0:
            ss[x][y-1]=ss[x][y]+1
            q.append((x,y-1))
    ans=max(ans,max(list(itertools.chain.from_iterable(ss))))
print(ans-1)