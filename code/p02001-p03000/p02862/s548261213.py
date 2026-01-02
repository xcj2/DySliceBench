import sys
input = sys.stdin.readline
X, Y = map(int, input().split())
mod = 10 ** 9 + 7
for t in range(X + Y + 1):
  if t == X + Y:
    print(0)
    exit(0)
  if X + Y - 2 * t == t:
    X -= t
    Y -= t
    break
if X < 0 or (Y < 0):
  print(0)
  exit(0)
class Factorial:
  def __init__(self, n, mod):
    self.f = [1]
    for i in range(1, n + 1):
      self.f.append(self.f[-1] * i % mod)
    self.i = [pow(self.f[-1], mod - 2, mod)]
    for i in range(1, n + 1)[: : -1]:
      self.i.append(self.i[-1] * i % mod)
    self.i.reverse()
  def factorial(self, i):
    return self.f[i]
  def ifactorial(self, i):
    return self.i[i]
  def combi(self, n, k):
    return self.f[n] * self.i[n - k] % mod * self.i[k] % mod
f = Factorial(X + Y, mod)
#print(X, Y)
print(f.combi(X + Y, X))