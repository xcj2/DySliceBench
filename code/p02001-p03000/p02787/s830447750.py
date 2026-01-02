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

H,N = II()
A,B = Line(N,2)

dp = [float('inf')]*(H+1)
dp[0] = 0
for i in range(1,H+1):
    for j in range(N):
        temp = i-A[j]
        if temp>=0:
            dp[i] = min(dp[i],dp[i-A[j]]+B[j])
        else:
            dp[i] = min(dp[i],dp[0]+B[j])

print(dp[-1])