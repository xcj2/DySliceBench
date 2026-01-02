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

N = I()
C = Line(N,1)

last = defaultdict(lambda:-1)

dp = [0]*N
dp[0] = 1
last[C[0]] = 0

for i in range(1,N):
    if C[i]==C[i-1]:
        dp[i] = dp[i-1]
    else:
        if last[C[i]]>=0:
            dp[i] = (dp[i-1] + dp[last[C[i]]])%mod
        else:
            dp[i] = dp[i-1]
    last[C[i]] = i

print(dp[-1])