class comb():
  F = [1, 1]
  Fi = [1, 1]
  I = [0, 1]
  def __init__(self, num, mod):
    self.MOD = mod
    for i in range(2, num + 1):
      self.F.append((self.F[-1] * i) % mod)
      self.I.append(mod - self.I[mod % i] * (mod // i) % mod)
      self.Fi.append(self.Fi[-1] * self.I[i] % mod)
  def com(self, n, k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return self.F[n] * (self.Fi[k] * self.Fi[n - k] % self.MOD) % self.MOD

def nasu(k, b):
  if k < b:
    return 0
  m = k - b
  return com.com((m + b - 1), m)

N, K = list(map(int, input().split()))
MOD = 10 ** 9 + 7

V = [0, 0, 0]
com = comb(N, MOD)
 
if K == N:
  V[0] = 1
V[1] = nasu(N - K, 1)
V[2] = nasu(N - K, 2)

for i in range(1, K + 1):
  t = com.com(K - 1, i - 1) 
  ans = t * (V[0] + V[2]) % MOD
  ans = (ans + t * V[1] * 2) % MOD
  print(ans)
  V[0] = V[1]
  V[1] = V[2]
  V[2] = nasu(N - K, i + 2)
