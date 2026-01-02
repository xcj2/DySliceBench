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

N,K = II()
H = III()

if N==K:
    print(0)
    exit()

dp = [[float('inf')]*(N-K+1) for _ in range(N)]

for x in range(N):
    for y in range(N-K+1):
        if x+1<y:
            continue
        elif y==0:
            dp[x][y] = float('inf')
        elif y==1:
            dp[x][y] = H[x]
        else:
            val = float('inf')
            for i in range(x):
                now = dp[i][y-1] + max(0,H[x]-H[i])
                if now<val:
                    val = now
            dp[x][y] = val

ans = float('inf')
for i in range(N):
    if dp[i][N-K]<ans:
        ans = dp[i][N-K]

print(ans)