import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

N,X = II()
l = [1]*(N+1)
for i in range(1,N+1):
    l[i] = l[i-1]*2+3

p = [1]*(N+1)
for i in range(1,N+1):
    p[i] = p[i-1]*2+1

#階層h，先頭i枚の中のパティの数
def rec(h,i):
    if h==0:
        if i>0:
            return 1
        else:
            return 0
    else:
        if i>=l[h]-1:
            return p[h]
        elif i<=1:
            return 0
        elif 2<=i<=l[h-1]+1:
            return rec(h-1,i-1)
        elif i==l[h-1]+2:
            return p[h-1]+1
        else:
            return p[h-1]+1+rec(h-1,i-l[h-1]-2)

print(rec(N,X))