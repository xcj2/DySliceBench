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
K = I()

S = str(N)
L = len(S)

# dp[i][x][f] : i桁目まで見て，0以外がx個ある総数
#              （f=1:N未満が確定，f=0:未確定）
dp = [[[0]*2 for _ in range(K+1)] for _ in range(L)]
dp[0][0][1] = 1
dp[0][1][0] = 1
dp[0][1][1] = int(S[0])-1

for i in range(1,L):
    for x in range(K+1):
        if S[i] == '0':
            dp[i][x][0] = dp[i-1][x][0]
            dp[i][x][1] = dp[i-1][x][1]
            if x >= 1:
                dp[i][x][1] += 9*dp[i-1][x-1][1]
        else:
            dp[i][x][1] = dp[i-1][x][0] + dp[i-1][x][1]
            if x >= 1:
                dp[i][x][0] = dp[i-1][x-1][0]
                dp[i][x][1] += 9*dp[i-1][x-1][1] + (int(S[i])-1)*dp[i-1][x-1][0]

print(dp[L-1][K][0]+dp[L-1][K][1])