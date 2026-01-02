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

R,C,K = LI()
r,c,v = LIR(K,3)

def index(i,j,k):
    return k*C*R + i*C + j

a = [[0]*C for _ in range(R)]
for i in range(K):
    a[r[i]-1][c[i]-1] = v[i]

dp = [0]*(4*C*R)
dp[index(0,0,1)] = a[0][0]

for i in range(R):
    for j in range(C):
        if i == j == 0:
            continue
        upper_max = 0
        if i >= 1:
            for k in range(4):
                upper_max = max(upper_max,dp[index(i-1,j,k)])
        for k in range(4):
            val1 = 0
            val2 = 0
            val3 = 0
            val4 = 0
            if j >= 1:
                val1 = dp[index(i,j-1,k)]
            if k == 0 and i >= 1:
                val2 = upper_max
            if a[i][j] != 0:
                if k == 1 and i >= 1:
                    val3 = upper_max + a[i][j]
                if k >= 1 and j >= 1:
                    val4 = dp[index(i,j-1,k-1)] + a[i][j]
            dp[index(i,j,k)] = max(val1,val2,val3,val4)

ans = 0
for k in range(4):
    ans = max(ans,dp[index(R-1,C-1,k)])

print(ans)