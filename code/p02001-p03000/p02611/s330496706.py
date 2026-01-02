class Lagrange:
  def __init__(self, lst):
    self.lst = lst
    self.mod = mod

  def prd(self, j, x):
    tmp = 1
    for i, (xi, yi) in enumerate(self.lst):
      if j != i:
        tmp *= (x - xi)
        tmp %= self.mod
    return tmp

  def pln(self, x):
    tmp = 0
    for i, (xi, yi) in enumerate(self.lst):
      tmp += yi * (self.prd(i, x) *
                   pow(self.prd(i, xi), self.mod - 2, self.mod))
      tmp %= self.mod
    return tmp

MAX = 40
mod = 10**9+7
fact = [1]*(MAX+1)
for i in range(1, MAX+1):
    fact[i] = (fact[i-1]*i) % mod

inv = [1]*(MAX+1)
for i in range(2, MAX+1):
    inv[i] = inv[mod % i]*(mod-mod//i) % mod

fact_inv = [1]*(MAX+1)
for i in range(1, MAX+1):
    fact_inv[i] = fact_inv[i-1] * inv[i] % mod

def comb(n, k):
    if n < k:
        return 0
    return fact[n] * fact_inv[n-k] * fact_inv[k] % mod

def f(n):
  tmp = 0
  for x in range(n):
    tmp += comb(x+4,4)*comb(n-2*x+5,10)
    tmp %= mod
  return tmp

c0 = [(i*2, f(i*2)) for i in range(16)]
c1 = [(i*2+1, f(i*2+1)) for i in range(16)]

a0 = Lagrange(c0)
a1 = Lagrange(c1)

t = int(input())
for _ in range(t):
  n = int(input())
  if n % 2 == 0:
    print(a0.pln(n))
  else:
    print(a1.pln(n))