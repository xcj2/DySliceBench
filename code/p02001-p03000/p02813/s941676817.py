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
p=list(map(int,input().split()))
q=list(map(int,input().split()))

for i in range(n):
    p[i]-=1
    q[i]-=1

com=list(permutations(range(n)))
# print(p,q)
a=0
b=0
for i in range(len(com)):
    # print(com[i])
    if com[i]==tuple(p):
        a=i
    if com[i]==tuple(q):
        b=i
print(abs(a-b))