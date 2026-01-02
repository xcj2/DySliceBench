X, Y = map(int, input().split())
Mod = 10 ** 9 + 7

def modpow(a, r, mod):
  k = 1
  for i in bin(r)[2:]:
    k = k ** 2 * a ** int(i)
    k %= mod
  return k

def fac(x, mod):
  k = 1
  for i in range(x):
    k *= i + 1
    k %= mod
  return k

def invfac(x, mod):
  k = modpow(fac(x, mod), mod-2, mod)
  return k  
  
def combi(n, r, mod):
  k = invfac(r, mod) * invfac(n-r, mod) * fac(n, mod)
  k %= mod
  return k
  
  
p = (2 * X - Y) // 3
q = (2 * Y - X) // 3
if (X + Y) % 3 != 0 or p < 0 or q < 0:
  print(0)
else:
  print(combi(p+q, p, Mod))
  
