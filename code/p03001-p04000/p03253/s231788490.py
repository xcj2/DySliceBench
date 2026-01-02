from collections import defaultdict as dd
N, M = map(int, input().split())
p = dd(int)
mod = 10 ** 9 + 7
maxps = 0
i = 2
while i <= 10 ** 9:
  if M <= 1:
    break
  while M % i == 0:
    p[i] += 1
    maxps = max(maxps, p[i])
    M //= i
  i += 1
if len(p.keys()) == 0 and M > 1:
  p[M] = 1
class Factorial:
  def __init__(self, n, mod):
    self.f=[1]
    for i in range(1, n + 1):
      self.f.append(self.f[-1] * i % mod)
    self.i=[pow(self.f[-1], mod - 2, mod)]
    for i in range(1, n + 1)[: : -1]:
      self.i.append(self.i[-1] * i % mod)
    self.i.reverse()
  def factorial(self, i):
    return self.f[i]
  def ifactorial(self, i):
    return self.i[i]
  def combi(self, n, k):
    return self.f[n] * self.i[n - k] % mod * self.i[k] % mod
res = 1
f = Factorial(maxps + N, mod)
for i in p.keys():
  res *= f.combi(p[i] + N - 1, p[i])
print(res % mod)