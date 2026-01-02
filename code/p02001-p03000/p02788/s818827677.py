#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

def ceil(x,y):
  return (x-1)//y+1


def solve_binary(mid,k):
    return k < XH[mid][0]

def binary_search(s,n,k):
    ok=n
    ng=s
    while abs(ok-ng)>1:
        mid=(ok+ng)//2
        if solve_binary(mid,k):
            ok=mid
        else:
            ng=mid
    return ok

n,D,A=map(int,input().split())
XH=[tuple(map(int,input().split())) for i in range(n)]
XH.sort(key=lambda tup: tup[0])
XH.append((inf,0))
data=[0]*(n+1)
# if D==0:
#     for xi,hi in XH:
#         count += ceil(hi,A)
#     print(count)
#     exit()
for i in range(n):
    xi,hi = XH[i]
    hi-=data[i]
    K=max(0,ceil(hi,A)*A); count += max(0,ceil(hi,A))
    data[i]+=K; data[binary_search(i,n,xi+2*D)]-=K
    data[i+1]+=data[i]
print(count)