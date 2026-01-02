from sys import stdin
input = stdin.readline


class PrimeComb:
  def __init__(self, MAX=510000, MOD=1000000007):
    self.MAX  = MAX
    self.MOD  = MOD
    self.fac  = [0]*MAX
    self.inv  = [0]*MAX
    self.finv = [0]*MAX
    self.fac[0]  = self.fac[1] = 1
    self.finv[0] = self.finv[1] = 1
    self.inv[1]  = 1
    for i in range(2, MAX):
      self.fac[i]  = self.fac[i-1] * i % MOD
      self.inv[i]  = MOD - self.inv[MOD % i] * int(MOD / i) % MOD
      self.finv[i] = self.finv[i-1] * self.inv[i] % MOD

  def com(self, n, k):
    # compute -> nCk % self.P
    if (n < k): return 0
    if (n < 0 or k < 0): return 0
    return self.fac[n] * (self.finv[k] * self.finv[n-k] % self.MOD) % self.MOD


def prime_fatorization(n):
  from collections import defaultdict
  # a = []
  a = defaultdict(int)
  while not(n % 2):
    # a.append(2)
    a[2] += 1
    n //= 2
  f = 3
  while f * f <= n:
    if not(n % f):
      # a.append(f)
      a[f] += 1
      n //= f
    else:
      f += 2
  if n != 1:
    # a.append(n)
    a[n] += 1
  return a


def main():
  N, M = list(map(int, input().split()))

  PC = PrimeComb(200000)
  P = prime_fatorization(M)
  ans = 1
  for k in P.values():
    ans *= PC.com(N-1+k, k)
    # print(N-1+k, 'C', k, PC.com(N-1+k, k))
  print(ans % 1000000007)


if(__name__ == '__main__'):
  main()