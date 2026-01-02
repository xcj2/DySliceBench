import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

N,K = LI()
L,R = LIR(K,2)

LR = [(L[i],R[i]) for i in range(K)]
LR.sort(key=lambda x:x[0])

L = [LR[i][0] for i in range(K)]
R = [LR[i][1] for i in range(K)]

S = [0]*K

dp = [0]*N
dp[0] = 1
for i in range(N):
    for k in range(K):
        if i > R[k]:
            S[k] += dp[i-L[k]] - dp[i-R[k]-1]
            S[k] %= mod
        elif i < L[k]:
            S[k] += 0
        else:
            S[k] += dp[i-L[k]]
            S[k] %= mod
        dp[i] += S[k]
        dp[i] %= mod


print(dp[-1])