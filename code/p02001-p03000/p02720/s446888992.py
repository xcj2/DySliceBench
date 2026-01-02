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

def dil(i):
    if 1<=i<=8:
        return [i-1,i,i+1]
    if i==0:
        return [0,1]
    if i==9:
        return [8,9]

K = I()

#dp[i][j][k]:i桁，スタートj,ラストk
dp = [[[0]*10 for _ in range(10)] for _ in range(12)]
for i in range(10):
    dp[1][i][i] = 1

for i in range(2,12):
    for j in range(10):
        for k in range(10):
            if 1<=k<=8:
                dp[i][j][k] = dp[i-1][j][k-1]+dp[i-1][j][k]+dp[i-1][j][k+1]
            if k==0:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j][k+1]
            if k==9:
                dp[i][j][k] = dp[i-1][j][k-1]+dp[i-1][j][k]

#dp2[i][j]: i桁，スタートjのルンルン数の総数
dp2 = [[0]*10 for _ in range(12)]
for i in range(12):
    for j in range(10):
        dp2[i][j] = sum(dp[i][j])

i = 1
aa = 0
while 1:
    if aa+sum(dp2[i][1:]) >= K:
        L = i
        break
    aa += sum(dp2[i][1:])
    i += 1

for i in range(L):
    K -= sum(dp2[i][1:])

temp = 0
now = 0
ans = ''
dl = [i for i in range(1,10)]
for l in range(L):
    last_j = dl[0]
    for j in dl:
        if temp+now+dp2[L-l][j]>=K:
            break
        else:
            now += dp2[L-l][j]
            last_j = j+1
    ans += str(last_j)
    temp = temp+now
    now = 0
    dl = dil(last_j)

print(int(ans))