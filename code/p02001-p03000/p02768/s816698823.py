n, a, b = map(int, input().split())

from operator import mul
from functools import reduce
import math

flg = (a == n-b)
rep = math.ceil(n/2)
MOD = 10**9+7
memo = 0

def modpow(a: int, p: int, mod: int) -> int:
    # return a**p (mod MOD) O(log p)
    if p == 0:
        return 1
    if p % 2 == 0:
        half = modpow(a, p//2, mod)
        return half*half % mod
    else:
        return a * modpow(a, p-1, mod) % mod


from operator import mul
from functools import reduce

def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mod_mul, range(n, n - r, -1), 1)
    denom = reduce(mod_mul, range(1, r + 1), 1)
    return numer*pow(denom, MOD-2, MOD)%MOD
  
def mod_mul(a, b):
  return mul(a%MOD, b%MOD)%MOD

s = 0
ans = modpow(2, n, MOD)-1
if flg:
  ans = ans - 2*combinations_count(n, a)%MOD
else:
  ans = (ans - combinations_count(n,a))%MOD - combinations_count(n,b)
print(ans%MOD)