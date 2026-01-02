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

class Inv:
  def __init__(s, mod):
    s.MOD = mod
  def modpow(s, a, n):
    res = 1
    while n > 0:
      if n & 1:
        res = res * a % s.MOD
      a = a * a % s.MOD
      n >>= 1
    return res
  def invx(s, a):
    return s.modpow(a, s.MOD - 2)
  def invL(s, a, n):
    ia = s.invx(a)
    L = [1] * (n + 1)
    for i in range(1, n + 1):
      L[i] = L[i - 1] * ia % s.MOD
    return L

n, a, b = list(map(int, input().split()))
MOD = 10 ** 9 + 7

inv = Inv(MOD)
com = comb(max(a, b) + 1, MOD)

ans = inv.modpow(2, n) - 1

def nasu(n, a):
  ans = 1
  for i in range(a):
    ans = ans * (n - i) * com.I[i + 1] % MOD
  return ans

ans = ans - nasu(n, a)
ans = ans - nasu(n, b)

while ans < 0:
  ans += MOD

print(ans)