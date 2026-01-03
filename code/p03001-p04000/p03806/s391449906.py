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

N,Ma,Mb = LI()
a,b,c = LIR(N,3)

amax = sum(a)
bmax = sum(b)

# dp[i][j][k]: 薬品iまで見て，Aがjグラム，Bがkグラムの最小予算
dp = [[[5000]*(bmax+1) for _ in range(amax+1)] for _ in range(N)]
dp[0][a[0]][b[0]] = c[0]
dp[0][0][0] = 0
for i in range(1,N):
    for j in range(amax+1):
        for k in range(bmax+1):
            if j == k == 0:
                dp[i][j][k] = 0
            elif j-a[i] < 0 or k-b[i] < 0:
                dp[i][j][k] = dp[i-1][j][k]
            else:
                dp[i][j][k] = min(dp[i-1][j][k], dp[i-1][j-a[i]][k-b[i]]+c[i])

ans = 5000
now = 1
while True:
    if Ma*now <= amax and Mb*now <= bmax:
        if dp[N-1][Ma*now][Mb*now] < ans:
            ans = dp[N-1][Ma*now][Mb*now]
        now += 1
    else:
        break

if ans == 5000:
    print('-1')
else:
    print(ans)