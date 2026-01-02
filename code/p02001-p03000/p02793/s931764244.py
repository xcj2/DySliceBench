N = int(input())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7

if N == 1:
  print(1)
  exit()

import math
def prime(x):
  p = {}
  cnt = 2
  Flag = True
  while Flag:
    last = math.ceil(x ** 0.5) 
    if cnt > last:
      break
    for i in range(cnt, last + 1):
      if x % i == 0:
        x //= i
        p[i] = 1
        cnt = i + 2
        while x % i == 0:
          x //= i
          p[i] += 1
        cnt = i + 1
        break
      if i == last:
        Flag = False
  if x != 1:
    p[x] = 1
  return p

def listgcd(L):
  p = prime(L[0])
  for i in range(1, len(L)):
    q = prime(L[i])
    for n in q:
      if n in p:
        p[n] = max(p[n], q[n])
      else:
        p[n] = q[n]
  return p

def listgcdmod(L, MOD):
  p = listgcd(L)
  t = 1
  for n in p:
    t = t * pow(n, p[n]) % MOD
  return t

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

t = listgcdmod(A, MOD)
inv = Inv(MOD)
ans = 0
for i in range(N):
  ans = (ans + t * inv.invx(A[i])) % MOD
print(ans)
