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

A,B,C,D = LI()

dp = [[0]*(D+1) for _ in range(C+1)]
dp[A][B] = 1

for i in range(A,C+1):
    for j in range(B,D+1):
        if i == A and j == B:
            continue
        dp[i][j] = (dp[i-1][j]*j)%mod + (dp[i][j-1]*i)%mod\
                     - (dp[i-1][j-1]*(i-1)*(j-1))%mod
        dp[i][j] %= mod

print(dp[C][D])