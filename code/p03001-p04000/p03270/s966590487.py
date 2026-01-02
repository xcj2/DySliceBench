from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

K, N = reads()
MOD = 998244353

MAXN = 4020

fact = [1] * MAXN
for i in range(1, MAXN): fact[i] = (fact[i-1] * i) % MOD
invfact = [0] * MAXN; invfact[-1] = pow(fact[-1], MOD-2, MOD)
for i in range(MAXN-2, -1, -1): invfact[i] = invfact[i+1] * (i+1) % MOD
def comb(n, k):
  return fact[n] * invfact[n-k] * invfact[k] % MOD if 0 <= k <= n else 0
def h(n, k):
  return comb(n+k-1, n)

def solve(n, k, u):
  ans = 0
  for q in range(u+1):
    ans = (ans + comb(u, q) * pow(2, u-q, MOD) % MOD * h(n-u+q, k-q-u)) % MOD
  return ans

anss = [0] * (2*K+1)
for i in range(2, K+2):
  u = sum(j < i-j <= K for j in range(1, K+1))
  if i % 2 == 1:
    ans = solve(N, K, u)
  else:
    ans = (solve(N, K-1, u) + solve(N-1, K-1, u)) % MOD
  anss[i] = ans
  print(ans)

for j in range(K+2, 2*K+1):
  print(anss[2*K - j + 2])
