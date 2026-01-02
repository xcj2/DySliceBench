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
b=list(map(int,input().split()))

sum_a=sum(a)
sum_b=sum(b)
if sum_a<sum_b:
    print(-1)
    exit()

lst=[]
cnt=0
ans=0
for i in range(n):
    if b[i]<=a[i]:
        lst.append(a[i]-b[i])
    else:
        cnt+=b[i]-a[i]
        ans+=1
# print(lst)
lst.sort()
# print(cnt)
# print(ans)
for i in range(len(lst))[::-1]:
    if cnt<=0:
        break
    cnt-=lst[i]
    ans+=1
print(ans)