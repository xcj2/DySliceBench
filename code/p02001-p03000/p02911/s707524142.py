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

N,K,Q = II()
A = [I() for _ in range(Q)]

count = [K-Q]*N

for i in range(Q):
    count[A[i]-1] += 1

ans = N
for i in range(N):
    if count[i]>0:
        print('Yes')
    else:
        print('No')