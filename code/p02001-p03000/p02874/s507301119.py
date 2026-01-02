import bisect
import copy
import heapq
import math
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n=int(input())
lr=[list(map(int,input().split())) for i in range(n)]
lr.sort()
# print(lr)

alst=[(lr[0][0],lr[0][1])]
blst=[(lr[-1][0],lr[-1][1])]
for i in range(n-1):
    alst.append((lr[i+1][0], min(alst[i][1],lr[i+1][1])))
    blst.append((max(blst[i][0],lr[-i-2][0]), min(blst[i][1],lr[-i-2][1])))
# print(alst)
# print(blst)
ans=0
def sa(lst):
    return max(0,lst[1]-lst[0]+1)

for i in range(n-1):
    ans=max(ans,sa(alst[i])+sa(blst[-i-2]))

lr2=sorted(lr,key=lambda x: x[1])
# print(lr2)
for i in range(n):
    tmp=sa(lr[i])
    l,r=0,0
    if lr[i][0]==lr[-1][0]:
        l=lr[-2][0]
    else:
        l=lr[-1][0]
    if lr[i][1]==lr2[0][1]:
        r=lr2[1][1]
    else:
        r=lr2[0][1]
    # print(tmp,l,r)
    ans=max(ans,tmp+max(0,r-l+1))
print(ans)