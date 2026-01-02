from operator import mul
from functools import reduce

n, a, b = map(int, input().split())

mod = 10 ** 9 + 7

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def power(x, y):
    if   y == 0     :
      return 1
    elif y == 1     :
      return x % mod
    elif y % 2 == 0 :
      return power(x, y//2)**2 % mod
    else            :
      return power(x, y//2)**2 * x % mod

def div(a, b):
    return mul(a, power(b, mod-2))

r1 = min(a, n - a)
r2 = min(b, n - b)

if r1 > r2:
  r1, r2 = r2, r1

numer1 = reduce(mul, range(n, n - r1, -1), 1)
denom1 = reduce(mul, range(1, r1 + 1), 1)
numer2 = reduce(mul, range(n - r1, n - r2, -1), numer1)
denom2 = reduce(mul, range(r1 + 1, r2 + 1), denom1)

print((power(2, n) - 1 - div(numer1, denom1) - div(numer2, denom2)) % (10 ** 9 + 7))
