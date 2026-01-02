from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

N = inp()
#dp[n][i][j][k] 全体でn文字あってn-1,n-2,n-3文字目がk,j,iであるパターン数
#0:A 1:C 2:G 3:T
dp = [[[[0 for i in range(4)] for j in range(4)] for k in range(4)] for l in range(N+5)]
for i in range(4):
    for j in range(4):
        for k in range(4):
            if (i,j,k) == (0,2,1) or (i,j,k) == (0,1,2) or (i,j,k) == (2,0,1):
                continue
            dp[3][i][j][k] = 1
# pprint.pprint(dp)
if N == 3:
    print(61)
    quit()
for n in range(4,N+1):
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if (j,k,l) == (0,2,1) or (i,k,l) == (0,2,1) or (i,j,l) == (0,2,1) or (j,k,l) == (2,0,1) or (j,k,l) == (0,1,2):
                        continue
                    dp[n][j][k][l] += dp[n-1][i][j][k]
                    dp[n][j][k][l] %= mod
res = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            res += dp[N][i][j][k]
            res %= mod
print(res)
# pprint.pprint(dp)
