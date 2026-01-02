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
def Line(N,num):
    if N<=0:
        for _ in range(num): return []
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list,zip(*read_all))

#################

H,W,D = II()
A = []
for _ in range(H):
    A.append(III())
Q = I()
L,R = Line(Q,2)

d = defaultdict(tuple)
for i in range(H):
    for j in range(W):
        d[A[i][j]-1] = (i,j)

a = [0]*(H*W)
for i in range(H*W)[::-1]:
    if i+D <= H*W-1:
        a[i] = a[i+D] + abs(d[i+D][0]-d[i][0]) + abs(d[i+D][1]-d[i][1])

for i in range(Q):
    print(a[L[i]-1]-a[R[i]-1])