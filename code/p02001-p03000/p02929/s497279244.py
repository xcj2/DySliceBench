N = int(input())
S = list(input())
L = [1]
cumsumL = [1]
res = 1
rvisited = 0
mod = 10 ** 9 + 7
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
f = Factorial(N, mod)
if S[0] == "W" or S[-1] == "W":
  print(0)
  exit(0)
for i in range(1, 2 * N):
  if S[i - 1] == S[i]:
    L.append((L[i - 1] + 1 )% 2)
  else:
    L.append(L[i - 1])
if sum(L) != N:
  print(0)
  exit(0)
for i in range(1, 2 * N):
  cumsumL.append(cumsumL[i - 1] + L[i])
for i in range(1, 2 * N):
  if L[i] == 0:
    res *= cumsumL[i] - rvisited % mod
    res %= mod
    rvisited += 1
print(f.factorial(N) * res % mod)