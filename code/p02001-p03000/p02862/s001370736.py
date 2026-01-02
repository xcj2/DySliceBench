# #二項係数(mod)
def comb(n, k, mod, fac, finv):
    if n < k or n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod

# 階乗の逆元(mod)
def factorials_inv_mod(n, mod):
    inv = [1] * (n + 1)
    factorials_inv = [1] * (n + 1)
    for i in range(2, n + 1):
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        factorials_inv[i] = factorials_inv[i - 1] * inv[i] % mod
    return factorials_inv

# 階乗(mod)
def factorials_mod(n, mod):
    factorials = [1] * (n + 1)
    for i in range(2, n+1):
        factorials[i] = (factorials[i-1] * i) % mod
    return factorials

MOD = 1000000007
x, y = map(int, input().split())
if (x + y) % 3 != 0:
  print(0)
  exit()
k = (x + y) // 3
fac = factorials_mod(k, MOD)
finv = factorials_inv_mod(k, MOD)
print(comb(k, x-k, MOD, fac, finv))