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

n,p=map(int,input().split())
a=list(map(int,input().split()))

lst=[0,0]

for i in range(n):
    lst[a[i]%2]+=1
# print(lst)

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

tmp1=pow(2,lst[0])
tmp2=0
for i in range(lst[1]+1):
    if p==0 and i%2==0:
        tmp2+=comb(lst[1],i)
    elif p==1 and i%2==1:
        tmp2+=comb(lst[1],i)
print(tmp1*tmp2)
# print(tmp1,tmp2)