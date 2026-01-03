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

h,w=map(int,input().split())
a=[input() for i in range(h)]

cnt=0
for i in range(h):
    for j in range(w):
        if a[i][j]=="#":
            cnt+=1
if cnt!=h+w-1 or a[0][0]!="#" or a[-1][-1]!="#":
    print("Impossible")
    exit()

now=[0,0]
for i in range(h+w-2):
    if now[0]+1<h and a[now[0]+1][now[1]]=="#":
        now[0]+=1
    elif now[1]+1<w and a[now[0]][now[1]+1]=="#":
        now[1]+=1
    else:
        print("Impossible")
        exit()
print("Possible")