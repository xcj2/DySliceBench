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

# 引かれる数の左からi桁目に+10 & 引く数のi-1桁目に+1 を適宜行う

def calc(x):
    if 0 <= x <= 5:
        return x
    else:
        return 10-x+1

S = list(input())
L = len(S)

dp0 = [0]*L
dp1 = [0]*L
dp0[0] = calc(int(S[0]))
dp1[0] = calc(int(S[0])+1)

for i in range(1,L):
    n = int(S[i])
    if n == 0:
        dp0[i] = dp0[i-1]
    else:
        dp0[i] = min(dp0[i-1]+n, dp1[i-1]+10-n)
    if n == 9:
        dp1[i] = dp1[i-1]
    else:
        dp1[i] = min(dp0[i-1]+n+1, dp1[i-1]+9-n)

print(dp0[-1])