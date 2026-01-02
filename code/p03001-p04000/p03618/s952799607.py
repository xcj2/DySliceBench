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
        return [[] for _ in range(num)]
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

A = str(input())
N = len(A)

d = defaultdict(int)

dp = [0]*N
dp[0] = 1
d[A[0]] = 1
for i in range(1,N):
    dp[i] = dp[i-1]+i-d[A[i]]
    d[A[i]] += 1

print(dp[-1])