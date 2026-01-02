from collections import defaultdict
from functools import reduce

n, a, b = map(int, input().split())

MOD = 10 ** 9 + 7

def mul(a, b):
  return ((a % MOD) * (b % MOD)) % MOD

def power(x, y):
  if y == 0:
    return 1
  elif y == 1:
    return x % MOD
  elif y % 2 == 0:
    return power(x, y // 2) ** 2 % MOD
  else:
    return mul(power(x, y // 2) ** 2, x)

def div(a, b):
  return mul(a, power(b, MOD - 2))

def dict1():
  return {0: 1}

numer_cache = defaultdict(dict1)
denom_cache = dict1()

def combinations_count(n, r):
  r = min(r, n - r)

  r2 = max(x for x in numer_cache[n] if x <= r)
  if r2 < r:
    numer_cache[n][r] = reduce(mul, range(n - r2, n - r, -1), numer_cache[n][r2])
  numer = numer_cache[n][r]

  r3 = max(x for x in denom_cache if x <= r)
  if r3 < r:
    denom_cache[r] = reduce(mul, range(r3 + 1, r + 1), denom_cache[r3])
  denom = denom_cache[r]

  return div(numer, denom)

r1 = min(a, n - a)
r2 = min(b, n - b)

if r1 > r2:
  r1, r2 = r2, r1

print((power(2, n) - 1 - combinations_count(n, r1) - combinations_count(n, r2)) % MOD)
