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
a=[input() for i in range(n)]
lst=[0]*n

def chenge(m):
    nn,mm=m.split(".")
    mm+=(9-len(mm))*"0"
    return int(nn+mm)

for i in range(n):
    if "." in a[i]:
        lst[i]=chenge(a[i])
    else:
        lst[i]=int(a[i]+9*"0")

# print(lst)

tf=[0]*n
for i in range(n):
    mm=lst[i]
    t,f=0,0
    while mm%2==0:
        t+=1
        mm//=2
    while mm%5==0:
        f+=1
        mm//=5
    tf[i]=(t,f)
# print(tf)

rui=[[0]*50 for i in range(50)]
for i in range(n):
    t,f=tf[i]
    rui[t][f]+=1

for i in range(49):
    for j in range(49):
        rui[48-i][48-j]+=rui[49-i][48-j]+rui[48-i][49-j]-rui[49-i][49-j]
# print(rui)

ans=0
for i in range(n):
    t,f=tf[i]
    ans+=rui[max(0,18-t)][max(0,18-f)]
    if t>=9 and f>=9:
        ans-=1
    # print(rui[max(0,18-t)][max(0,18-f)])
print(ans//2)