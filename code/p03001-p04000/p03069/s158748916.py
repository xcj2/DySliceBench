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
S = str(input())

dp = [0]*(N+1)
temp = 0
for i in range(N):
    if S[i] == '.':
        temp += 1

dp[0] = temp

for i in range(1,N+1):
    if S[i-1] == '.':
        dp[i] = dp[i-1]-1
    else:
        dp[i] = dp[i-1]+1

print(min(dp))