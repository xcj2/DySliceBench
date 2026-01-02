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

from bisect import bisect_left, bisect_right

A,B,Q = II()
s = [I() for _ in range(A)]
t = [I() for _ in range(B)]
x = [I() for _ in range(Q)]

for i in range(Q):
    val = float('inf')
    a = bisect_left(s,x[i])
    if a<=A-1:
        b = bisect_left(t,s[a])
        if b<=B-1:
            val = min(val, abs(x[i]-s[a]) + abs(s[a]-t[b]))
        if b>=1:
            val = min(val, abs(x[i]-s[a]) + abs(s[a]-t[b-1]))
    if a>=1:
        b = bisect_left(t,s[a-1])
        if b<=B-1:
            val = min(val, abs(x[i]-s[a-1]) + abs(s[a-1]-t[b]))
        if b>=1:
            val = min(val, abs(x[i]-s[a-1]) + abs(s[a-1]-t[b-1]))

    b = bisect_left(t,x[i])
    if b<=B-1:
        a = bisect_left(s,t[b])
        if a<=A-1:
            val = min(val, abs(x[i]-t[b]) + abs(t[b]-s[a]))
        if a>=1:
            val = min(val, abs(x[i]-t[b]) + abs(t[b]-s[a-1]))
    if b>=1:
        a = bisect_left(s,t[b-1])
        if a<=A-1:
            val = min(val, abs(x[i]-t[b-1]) + abs(t[b-1]-s[a]))
        if a>=1:
            val = min(val, abs(x[i]-t[b-1]) + abs(t[b-1]-s[a-1]))
    
    print(val)