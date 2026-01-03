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

from bisect import bisect_right

N,W = LI()
w,v = LIR(N,2)

w_list = []
for i in range(N+1):
    for j in range(i*w[0],i*(w[0]+3)+1):
        w_list.append(j)
w_list = sorted(list(set(w_list)))
M = len(w_list)

d = {}
temp = 0
for wl in w_list:
    d[temp] = wl
    temp += 1

dp = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        dp[i][j] = dp[i-1][j]
        x = d[j]-w[i]
        if x >= 0:
            p = bisect_right(w_list,x)
            dp[i][j] = max(dp[i][j], dp[i-1][p-1]+v[i])

p = bisect_right(w_list,W)
print(dp[N-1][p-1])