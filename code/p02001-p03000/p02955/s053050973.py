import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product
# from math import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,k=map(int,input().split())
a=list(map(int,input().split()))


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

divs=make_divisors(sum(a))
# print(divs)
ans=1
for i in range(len(divs)):
    r=[]
    d=divs[i]
    for j in range(n):
        if a[j]%d!=0:
            r.append(a[j]%d)
    r.sort()

    ruir=ruiseki(r)
    # print(d,ruir)
    # print(r)
    if ruir==[0]:
        ans=d
    for i in range(len(r)):
        hiku=ruir[i]
        tasu=-(ruir[-1]-ruir[i])+d*(len(r)-i)
        # print(hiku,tasu,ruir[-1]-ruir[i])
        if hiku%d==tasu%d and max(hiku,tasu)<=k:
            ans=d

print(ans)