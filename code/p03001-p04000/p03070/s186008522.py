import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
import numpy as np

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 998244353

def power(x, y):
   if y == 0:
       return 1
   elif y == 1:
       return x % mod
   elif y % 2 == 0:
       return power(x, y/2) ** 2 % mod
   else:
       return power(x, (y-1)/2) ** 2 * x % mod

N = INT()
a = np.array([INT() for _ in range(N)])

sum_a = np.sum(a)
dp = np.zeros((N+1, sum_a+1))
dp[0][0] = 1

dp2 = np.zeros((N+1, sum_a//2+1))
dp2[0][0] = 1

for i, x in enumerate(a):
	dp[i+1, :] += dp[i, :]*2 % mod # 赤以外に塗り分ける
	dp[i+1, x:] += dp[i, :-x] % mod # 赤に塗り分ける
	dp2[i+1,:] += dp2[i, :] % mod
	dp2[i+1, x:] += dp2[i, :-x] % mod
# print(dp)
# print(dp2)
if sum_a%2 == 0:
	print(int((power(3, N)-3*np.sum(dp[N,sum_a//2:])+3*dp2[N,sum_a//2])%mod))
else:
	print(int((power(3, N)-3*np.sum(dp[N,sum_a//2+1:]))%mod))
