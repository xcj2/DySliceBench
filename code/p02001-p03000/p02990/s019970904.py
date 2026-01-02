N, K = [int(i) for i in input().split()]

R = N - K
MOD = 10**9 + 7 

def mod_pow(a, n, mod):
  res = 1
  while  n > 0:
    if n & 1:
      res = (res * a ) % mod
    a = a * a  % mod
    n = n >> 1
  return res

class nCk_table:
  def __init__(self, MAX_N, mod=MOD):
    self.mod = mod
    self.MAX_N = MAX_N
    fact = [1]
    fact_inv = [0]*(MAX_N + 4)
    for i in range(MAX_N + 3):
      fact.append(fact[-1]*(i+1)%mod)

    fact_inv[-1] = mod_pow(fact[-1], mod-2, mod)
    for i in range(MAX_N+2,-1,-1):
        fact_inv[i] = fact_inv[i+1]*(i+1)%mod
    self.fact = fact
    self.fact_inv = fact_inv

  def __call__(self, n, k):
      return (((self.fact[n] * self.fact_inv[k]) % self.mod) * self.fact_inv[n-k]) % self.mod    

nCk = nCk_table(N + 1)

for k in range(K):
  I = k + 1
  if R < I - 1:
    print(0)
  else:
    print((nCk(R + 1, I) * nCk(K  - 1, I - 1)) % MOD)
  


