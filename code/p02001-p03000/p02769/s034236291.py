from collections import defaultdict
from functools import reduce

n, k = map(int, input().split())

MOD = 10 ** 9 + 7

def mul(a, b):
  return a * b % MOD

def power(x, y):
  res = 1
  while True:
    if y & 1:
      res = res * x % MOD
    if y == 1:
      return res
    x = x * x % MOD
    y >>= 1

def div(a, b):
  return a * power(b, MOD - 2) % MOD

def dict1():
  return {0: 1}

numer_cache = defaultdict(dict1)
denom_inv_cache = dict1()

def combinations_count(n, r):
  r = min(r, n - r)
  numer_cache_n = numer_cache[n]
  if r not in numer_cache_n:
    numer_cache_n[r] = mul(numer_cache_n[r - 1], n - r + 1)
  if r not in denom_inv_cache:
    denom_inv_cache[r] = div(denom_inv_cache[r - 1], r)
  return mul(numer_cache_n[r], denom_inv_cache[r])

print(sum(mul(combinations_count(n, i), combinations_count(n - 1, i)) for i in range(min(n, k + 1))) % MOD)
