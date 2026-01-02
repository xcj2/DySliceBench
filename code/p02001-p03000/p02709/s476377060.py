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

N = I()
A = LI()

Anew = []
for i in range(N):
    Anew.append((A[i],i))
Anew.sort(key=lambda x:(-x[0],x[1]))

dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue
        if i+j > N:
            continue
        elif i == 0:
            dp[i][j] = dp[i][j-1] + abs(Anew[j-1][1]-(N-j))*Anew[j-1][0]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + abs(Anew[i-1][1]-(i-1))*Anew[i-1][0]
        else:
            val1 = dp[i][j-1] + abs(Anew[i+j-1][1]-(N-j))*Anew[i+j-1][0]
            val2 = dp[i-1][j] + abs(Anew[i+j-1][1]-(i-1))*Anew[i+j-1][0]
            dp[i][j] = max(val1,val2)

ans = 0
for i in range(N):
    if dp[i][N-i] >= ans:
        ans = dp[i][N-i]

print(ans)