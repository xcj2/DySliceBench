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

n=int(input())
abc=[list(map(int,input().split())) for i in range(n-1)]
q,k=map(int,input().split())
xy=[list(map(int,input().split())) for i in range(q)]

itta=[0]*(n+1)
dic=defaultdict(list)
for a,b,c in abc:
    dic[a].append((b,c))
    dic[b].append((a,c))

d=deque([(k,0)])
while d:
    now=d.popleft()
    if itta[now[0]]!=0:
        continue
    itta[now[0]]=now[1]
    for i,j in dic[now[0]]:
        d.append((i,j+now[1]))
# print(itta)
itta[k]=0
for x,y in xy:
    print(itta[x]+itta[y])