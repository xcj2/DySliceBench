import os
import sys
import math
import heapq
from decimal import *
from io import BytesIO, IOBase
from collections import defaultdict, deque

def r():
    return int(input())
def rm():
    return map(int,input().split())
def rl():
    return list(map(int,input().split()))

n,k = rm()
p = rl()
p = [0]+p
c = rl()
c = [0]+c
b = [-1]*(n+1)
give=0
ans=-math.inf

for i in range(1,n+1):
    a=i
    lenn=1
    add=c[i]
    while p[a]!=i:
        add+=c[p[a]]
        lenn+=1
        a=p[a]
    if add<0:
        add=0
    addAgain=0
    a=i
    for j in range(lenn):
        if j>k:
            break
        addAgain+=c[a]
        ans = max(ans, addAgain+add*((k-j-1)//lenn))
        a = p[a]

print(ans)