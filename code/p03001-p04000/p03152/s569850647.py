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

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

dic_a={}
dic_b={}
for i in range(n):
    if a[i] in dic_a:
        print(0)
        exit()
    dic_a[a[i]]=1

for i in range(m):
    if b[i] in dic_b:
        print(0)
        exit()
    dic_b[b[i]]=1
# print(n*m)
ans=1
anum=0
bnum=0
for i in range(n*m):
    num=n*m-i
    if num in dic_a:
        if num in dic_b:
            bnum+=1
        else:
            ans*=bnum
        anum+=1
    else:
        if num in dic_b:
            ans*=anum
            bnum+=1
        else:
            ans*=anum*bnum-i
    ans%=mod
    # print(anum,bnum)
print(ans)