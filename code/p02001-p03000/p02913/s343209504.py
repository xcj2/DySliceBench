import random
import string
N = int(input())
S = input()
l, r = 0, N

def pow_mod(a, b, m):
  ab = 1
  for _ in range(b):
    ab = (ab * a) % m
  return ab

def c2n(c):
  return ord(c) - 97

def hash(s, B, H):
  sh = 0
  for c in s:
    sh = (sh * B + c2n(c)) % H
  return sh

def t(n):
  B, H = 10 ** 8 + 7, 2 ** 64

  if n*2 > N:
    return False
  s, t = S[:n], S[n:n*2]
  sh, th = hash(s, B, H), hash(t, B, H)
  if sh == th:
    return True
  ss = set([sh])
  Bn = pow_mod(B, n, H)
  for i in range(0, N-2*n):
    sh = (sh * B - c2n(S[i]) * Bn + c2n(S[i+n])) % H
    th = (th * B - c2n(S[i+n]) * Bn + c2n(S[i+2*n])) % H
    ss.add(sh)
    if th in ss:
      return True
  return False

while l+1<r:
  m = (l+r)//2
  if t(m):
    l=m
  else:
    r=m

print(l)