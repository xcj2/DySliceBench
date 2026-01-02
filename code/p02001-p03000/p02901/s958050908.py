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

N,M = II()
a = [0]*M
b = [0]*M
c = []
x = []
for i in range(M):
    a[i],b[i] = II()
    new_c = III()
    c.append(new_c)
    k = 0
    for c1 in new_c:
        k += 2**(c1-1)
    x.append(k)

dp = [-1]*(2**N)
dp[0] = 0
for i in range(M):
    if dp[x[i]]==-1:
        dp[x[i]] = a[i]
    else:
        dp[x[i]] = min(dp[x[i]], a[i])
    for j in range(2**N-1):
        if dp[j]==-1:
            continue
        else:
            if dp[j|x[i]]==-1:
                dp[j|x[i]] = dp[j] + dp[x[i]]
            else:        
                dp[j|x[i]] = min(dp[j|x[i]], dp[j] + dp[x[i]])

print(dp[2**N-1])