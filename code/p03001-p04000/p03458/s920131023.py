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


n,k=map(int,input().split())
xyc=[list(input().split()) for i in range(n)]

ww=[[0]*(2*k+1) for i in range(2*k+1)]
bb=[[0]*(2*k+1) for i in range(2*k+1)]

for i in range(n):
    x,y,c=xyc[i]
    x,y=int(x),int(y)
    if c=="W":
        ww[x%(2*k)+1][y%(2*k)+1]+=1
    else:
        bb[x%(2*k)+1][y%(2*k)+1]+=1

for i in range(2*k):
    for j in range(2*k):
        ww[i+1][j+1]=ww[i+1][j+1]+ww[i+1][j]+ww[i][j+1]-ww[i][j]
        bb[i+1][j+1]=bb[i+1][j+1]+bb[i+1][j]+bb[i][j+1]-bb[i][j]
# print(ww)

def cnt(i1,i2,j1,j2,lst):
    return lst[i2+1][j2+1]-lst[i1+1][j2+1]-lst[i2+1][j1+1]+lst[i1+1][j1+1]

ans=0
for i in range(k+1):
    for j in range(k+1):
        w,b=0,0
        # 左下
        w+=cnt(-1, i-1, -1, j-1, ww)
        # 中央
        w+=cnt(i-1, i+k-1, j-1, j+k-1, ww)
        # 左上
        w+=cnt(-1, i-1, j+k-1, 2*k-1, ww)
        # 右下
        w+=cnt(i+k-1, 2*k-1, -1, j-1, ww)
        # 右上
        w+=cnt(i+k-1, 2*k-1, j+k-1, 2*k-1, ww)

        b+=cnt(-1, i-1, j-1, j+k-1, bb)
        b+=cnt(i-1, i+k-1, -1, j-1, bb)
        b+=cnt(i+k-1, 2*k-1, j-1, j+k-1, bb)
        b+=cnt(i-1, i+k-1, j+k-1, 2*k-1, bb)
        # print(w,b)
        ans=max(ans,w+b)
ww,bb=copy.deepcopy(bb),copy.deepcopy(ww)
for i in range(k+1):
    for j in range(k+1):
        w,b=0,0
        # 左下
        w+=cnt(-1, i-1, -1, j-1, ww)
        # 中央
        w+=cnt(i-1, i+k-1, j-1, j+k-1, ww)
        # 左上
        w+=cnt(-1, i-1, j+k-1, 2*k-1, ww)
        # 右下
        w+=cnt(i+k-1, 2*k-1, -1, j-1, ww)
        # 右上
        w+=cnt(i+k-1, 2*k-1, j+k-1, 2*k-1, ww)

        b+=cnt(-1, i-1, j-1, j+k-1, bb)
        b+=cnt(i-1, i+k-1, -1, j-1, bb)
        b+=cnt(i+k-1, 2*k-1, j-1, j+k-1, bb)
        b+=cnt(i-1, i+k-1, j+k-1, 2*k-1, bb)
        # print(w,b)
        ans=max(ans,w+b)
print(ans)