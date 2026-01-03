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

h,w,n=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]

itta={}
dic={}
for a,b in ab:
    dic[(a,b)]=1
def seek(t,y):
    if (not (t,y) in itta) and 2<=t<h and 2<=y<w:
        itta[(t,y)]=1
        cnt=0
        for i in range(3):
            for j in range(3):
                cnt+=(t-1+i,y-1+j) in dic
        return cnt
    else:
        return 0

lst=[0]*10
for i in range(n):
    a,b=ab[i]
    for i in range(3):
        for j in range(3):
            cnt=seek(a-1+i,b-1+j)
            if cnt:
                lst[cnt]+=1

# print(lst)
# sumlst=sum(lst)
lst[0]=(h-2)*(w-2)-sum(lst)
for i in range(10):
    print(lst[i])