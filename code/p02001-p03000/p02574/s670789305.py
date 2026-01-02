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
a=list(map(int,input().split()))
pc="pairwise coprime"
sc="setwise coprime"
nc="not coprime"
a.sort()
tmp=a[0]

for i in range(n):
    tmp=math.gcd(tmp,a[i])
if tmp!=1:
    print(nc)
    exit()

dic={}
for i in range(n):
    if a[i] in dic:
        dic[a[i]]+=1
    else:
        dic[a[i]]=1

ans=0
for i in range(a[-1]):
    now=i+1
    cnt=0
    # print(i)
    while now<=a[-1]:
        if now in dic:
            cnt+=dic[now]
        now+=i+1
    if cnt>1:
        ans=i+1

if ans!=1:
    print(sc)
else:
    print(pc)
# print(ans)