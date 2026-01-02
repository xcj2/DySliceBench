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

# Implementation
# class ModInt:
#     def __init__(self, n, MOD):
#         self.n = n
#         self.MOD = MOD
    
#     def __add__(self, o):
#         return ModInt((self.n + o.n) % self.MOD, self.MOD)

#     def __sub__(self, o):
#         return ModInt((self.n - o.n + self.MOD) % self.MOD, self.MOD)

#     def __mul__(self, o):
#         return ModInt((self.n * o.n) % self.MOD, self.MOD)

#     def __iadd__(self, o):
#         self.n = (self.n + o.n) % self.MOD
#         return self

#     def __isub__(self, o):
#         self.n = (self.n - o.n + self.MOD) % self.MOD
#         return self

#     def __imul__(self, o):
#         self.n = (self.n * o.n) % self.MOD
#         return self

#     def __str__(self): return str(self.n)

MOD = 998244353
N, S = read_tupple()
A = read_array()

dp = [[0 for j in range(S+1)] for i in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(S+1):
        dp[i + 1][j] = (dp[i + 1][j] + 2 * dp[i][j]) % MOD
        if j - A[i] >= 0:
            dp[i + 1][j] = (dp[i + 1][j] + dp[i][j - A[i]]) % MOD
print(dp[N][S])