import bisect, copy, heapq, math, sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
def celi(a,b):
    return -(-a//b)
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,m=map(int,input().split())
py=[list(map(int,input().split())) for i in range(m)]
for i in range(m):
    py[i].append(i)

py.sort()
anslst=[""]*m
dic=defaultdict(int)

for i in range(m):
    p,y,index=py[i]
    dic[p]+=1
    pnum=str(p)
    pnum="0"*(6-len(pnum))+pnum
    ynum=str(dic[p])
    ynum="0"*(6-len(ynum))+ynum
    anslst[index]=pnum+ynum
for i in range(m):
    print(anslst[i])