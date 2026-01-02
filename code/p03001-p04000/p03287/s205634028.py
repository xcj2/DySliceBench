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

N,M = II()
A = III()

a = [0]*(N+1)
for i in range(1,N+1):
    a[i] = a[i-1]
    a[i] += A[i-1]
    a[i] %= M

d = defaultdict(list)
for i in range(N+1):
    d[a[i]].append(i)

ans = 0
for k in d.keys():
    if len(d[k]) >= 2:
        ans += len(d[k])*(len(d[k])-1)//2

print(ans)