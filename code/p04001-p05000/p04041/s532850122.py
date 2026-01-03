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

N,X,Y,Z = II()

max_val = (1<<17)-1
dp = [[0]*(max_val+1) for _ in range(N+1)]

for k in range(1,11):
    dp[1][1<<(k-1)] = 1

for i in range(1,N):
    for j in range(1,max_val+1):
        for k in range(1,11):
            val = ((j<<k) + (1<<(k-1))) & max_val
            if (val>>(Z-1)&1) and (val>>(Z+Y-1)&1) and (val>>(Z+Y+X-1)&1):
                continue
            else:
                dp[i+1][val] += dp[i][j]
                dp[i+1][val] %= mod

temp = 0
for j in range(1,max_val+1):
    temp += dp[N][j]
    temp %= mod

ans = (pow(10,N,mod)-temp)%mod
print(ans)