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
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

N,x = II()
a = III()

dp = [[float('inf')]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if j==0:
            dp[i][j] = a[i]
        else:
            dp[i][j] = min(dp[i][j-1], a[(i-j)%N])

ans = float('inf')
for j in range(N):
    now = j*x
    for i in range(N):
        now += dp[i][j]
    if now<ans:
        ans = now

print(ans)