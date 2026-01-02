n, k= [int(i) for i in input().split()]
mod = 10**9 + 7

n_max = 4 * 10**5
fac = [1 for _ in range(n_max)]
inv = [1 for _ in range(n_max)]
finv = [1 for _ in range(n_max)]
def init():
  for i in range(2, n_max):
    fac[i] = fac[i - 1] * i % mod
    inv[i] = mod - inv[mod % i] * (mod // i) % mod
    finv[i] =finv[i-1] * inv[i] % mod    
  
def nCk(n, k, mod):
  return (fac[n] * finv[k] % mod)* finv[n-k] % mod
  
def nHm(n, m, mod):
  return nCk(n+m-1, m, mod)

init()
total = 1
n_max = min(n, k + 1)
for m in range(1, n_max):
  diff = nCk(n, m, mod) * nHm(n - m, m, mod) % mod
  total = total + diff
  

print(total % mod)
