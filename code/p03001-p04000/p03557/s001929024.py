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

from bisect import bisect_left

N = I()
A = III()
B = III()
C = III()

A.sort()
B.sort()
C.sort()

memo = [0]*N
for i in range(N):
    x = bisect_left(A,B[i])
    if i==0:
        memo[i] = x
    else:
        memo[i] = memo[i-1]+x

ans = 0
for i in range(N):
    y = bisect_left(B,C[i])
    if y==0:
        continue
    else:
        ans += memo[y-1]

print(ans)