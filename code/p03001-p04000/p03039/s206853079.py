N, M, K = list(map(int, input().split()))

MOD = int(1e9 + 7)
NM = N * M

def su(n):
  return n * (n + 1) // 2
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

co = comb(NM, MOD)
times = co.com(NM - 2, K - 2)
Ans = 0
for i in range(N):
  for j in range(M):
    k = (su(i) + su(N - i - 1)) * M
    k = k + (su(j) + su(M - j - 1)) * N
    k = k * times
    Ans += k

print(Ans // 2 % MOD)

