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


r1, c1, r2, c2 = list(map(int, input().split()))
MOD = 10 ** 9 + 7

def nasu(n, m):
  if n < 0 or m < 0: return 0
  ans = (com.com(n + 2, m + 1) - 1)
  return ans
N = r2 + c2
com = comb(N + 3, MOD)

ans = nasu(N, r2)
ans = (ans + nasu(c1 + r1 - 2, min(c1, r1) - 1)) % MOD
ans = (ans - nasu(r2 + c1 - 1, c1 - 1))
ans = (ans - nasu(c2 + r1 - 1, r1 - 1))
while ans < 0: ans += MOD

print(ans)