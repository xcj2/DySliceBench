# Import
from collections import deque
import math

# I/O
def read(): return input()
def read_int(): return int(input())
def read_array(type=int): return [type(i) for i in input().split()]
def read_tupple(type=None):
    tmp = input().split()
    if type is None: return map(int, tmp)
    assert len(tmp) == len(type)
    return [type[i](tmp[i]) for i in range(len(tmp))]

MOD = 998244353
N, S = read_tupple()
A = read_array()

dp = [[0 for j in range(S+1)] for i in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(S+1):
        dp[i + 1][j] += 2 * dp[i][j]
        if j - A[i] >= 0:
            dp[i + 1][j] += dp[i][j - A[i]]
        
        while dp[i+1][j] > MOD:
            dp[i+1][j] -= MOD
        
print(dp[N][S])
