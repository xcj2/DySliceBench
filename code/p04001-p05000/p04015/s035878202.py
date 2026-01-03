import sys
import math
from collections import defaultdict

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

N,A = LI()
x = LI()

# dp[i][j][k]：i枚目まで見て，j枚のカードを使って，和がk
dp = [[[0]*(50*N+1) for _ in range(N+1)] for _ in range(N)]
dp[0][0][0] = 1
dp[0][1][x[0]] = 1

for i in range(1,N):
    for j in range(N+1):
        for k in range(50*N+1):
            dp[i][j][k] = dp[i-1][j][k]
            if k-x[i] >= 0:
                dp[i][j][k] += dp[i-1][j-1][k-x[i]]

ans = 0
for j in range(1,N+1):
    ans += dp[N-1][j][A*j]

print(ans)