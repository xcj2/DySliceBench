#!/usr/bin/env python3
import sys
import heapq
input = lambda: sys.stdin.buffer.readline()[:-1].decode('utf-8')
sys.setrecursionlimit(10**8)
inf = float('inf')
mod = 10**9+7

n,m=map(int,input().split())
LRC=[list(map(int,input().split())) for i in range(m)]
LRC.sort(key=lambda tup:tup[1])

#####segfunc######
def segfunc(x,y):
   return min(x,y)


def init(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1] = init_val[i]
    #built
    for i in range(num-2, -1, -1):
        seg[i] = segfunc(seg[2*i+1], seg[2*i+2])


def update(k, x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = segfunc(seg[k*2+1], seg[k*2+2])


def query(p, q):
    if q <= p:
        return ide_ele
    p += num-1
    q += num-2
    res = ide_ele
    while q-p > 1:
        if p & 1 == 0:
            res = segfunc(res, seg[p])
        if q & 1 == 1:
            res = segfunc(res, seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res, seg[p])
    else:
        res = segfunc(segfunc(res, seg[p]), seg[q])
    return res


#####単位元######
ide_ele =inf

#num:n以上の最小の2のべき乗
num = 2**(n-1).bit_length()
seg = [ide_ele]*2*num

dp=[inf]*(n)
dp[0]=0

init(dp)



for L,R,C in LRC:
    L-=1;R-=1
    # print(query(L, R))
    dp[R] = min(dp[R], query(L, R)+C)
    update(R, dp[R])

print(dp[n-1] if dp[n-1]!=inf else -1)
# print(dp[:10])

