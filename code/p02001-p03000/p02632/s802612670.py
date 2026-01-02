from math import factorial

def combinations_count(n, r):
    ''' 組み合わせ '''
    return factorial(n) // (factorial(n - r) * factorial(r))

#print(combinations_count(5, 2))
def modpow(a, n, MOD):
  res = 1
  while (n > 0):
    if (n & 1):
      res = res * a % MOD
    a = a * a % MOD
    n >>= 1
  return res

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
mod = 10 ** 9 + 7
N = 2 * 10 ** 6 + 1  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

K = int(input())
S = str(input())
N = len(S)

ans = 0
p = N + K - 1
#now = combinations_count(p, N - 1) % mod

for i in range(K + 1):
  p = N + K - i - 1
  now = cmb(p, N - 1, mod)
  a = pow(25, K - i, mod)
  b = pow(26, i, mod)
  c = a * b % mod
  ans += now * c % mod
  ans = ans % mod
print(ans)
  