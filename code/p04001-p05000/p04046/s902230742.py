MOD = 10**9+7

def modpow(base, pow, mod):
  res = 1
  while pow > 0:
    if pow & 1:
      res = res * base % mod
    base = base**2 % mod
    pow >>= 1
  return res

def modmul(a, b, mod):
  return a*b % mod

def solve(h,w,a,b):
  fact = [0]*(h+w+1)
  fact[0] = 1
  fact_inv = [0]*(h+w+1)
  fact_inv[0] = 1
  for i in range(1, h+w):
    fact[i] = fact[i-1]*i % MOD
    fact_inv[i] = modpow(fact[i], MOD-2, MOD)

  ans = 0
  for col_idx in range(b, w):
    before_checkpoint = modmul(modmul(fact[h-a-1+col_idx], fact_inv[h-a-1], MOD), fact_inv[col_idx], MOD)
    from_checkpoint = modmul(modmul(fact[(a-1) + (w-col_idx-1)], fact_inv[w-col_idx-1], MOD), fact_inv[a-1], MOD)
    ans = (ans + modmul(before_checkpoint, from_checkpoint, MOD)) % MOD

  return ans

if __name__ == "__main__":
  h,w,a,b = map(int, input().split())
  print(solve(h,w,a,b))
