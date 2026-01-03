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
sys.setrecursionlimit(500000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,m=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n)]


def check(dic):
    lst=[0]*m
    for i in range(n):
        for j in range(m):
            if dic[a[i][j]]==1:
                lst[a[i][j]-1]+=1
                break
    maxl=max(lst)
    # print(dic,maxl,lst)
    if maxl==0:
        return n
    for i in range(m):
        if lst[i]==maxl:
            dic[i+1]=0
            break

    return min(maxl,check(dic))


dic={}
for i in range(m):
    dic[i+1]=1
# print(dic)
print(check(dic))