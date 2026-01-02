import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

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

S = I()
L = S//3
dp = [[0]*(S+1) for _ in range(L+1)]

for i in range(L+1):
    if i == 0:
        for j in range(3,S+1):
            dp[i][j] = 1
    else:
        val = dp[i-1][0]
        for j in range(3,S+1):
            dp[i][j] = val
            val += dp[i-1][j-2]
            val %= mod

ans = 0
for i in range(L+1):
    ans += dp[i][S]
    ans %= mod
print(ans)