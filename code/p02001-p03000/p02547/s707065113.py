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
d=[list(map(int,input().split())) for i in range(n)]

for i in range(n-2):
    d11,d12=d[i]
    d21,d22=d[i+1]
    d31,d32=d[i+2]
    if d11==d12 and d21==d22 and d31==d32:
        print("Yes")
        exit()

print("No")