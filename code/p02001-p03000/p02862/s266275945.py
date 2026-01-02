MOD = 1000000007

def mod(n):         
  return n % MOD

def add(a, b):      #mod(a+b)を求める
  return mod(mod(a)+mod(b))

def subtract(a, b): #mod(a-b)を求める
  return mod(mod(a)-mod(b))

def multiply(a, b): #mod(a*b)を求める
  return mod(mod(a)*mod(b))

def divide(a, b):   #mod(a / b)を求める
  ans = mod(a) * inverse(b)
  return mod(ans)

def modpow(a, n):   #mod(a**n)を高速で求める
    res = 1  
    digit = len(str(bin(n))) - 2
    for i in range(digit):
      if (n >> i) & 1:
        res *= mod(a)
        res = mod(res)
      a = mod(a**2)
    return mod(res)

def inverse(a):     #aの逆元を求める
  return modpow(a, MOD-2)

MAX = 1000000           #適当な数を入力
fac, finv, inv = [[0]*MAX for i in range(3)]
def combinit():     #MAXまでの下準備
  fac[0] = fac[1] = 1
  finv[0] = finv[1] = 1
  inv[1] = 1
  for i in range(2, MAX):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD

def modcomb(n, k):      #mod(nCk)を計算、ただしn<MAX
  if (n < k):
    return 0
  if (n < 0 or k < 0):
    return 0
  return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD
combinit()          #下準備の実行 O(MAX)

import sys
x, y = map(int, input().split())

if (x+y) % 3 != 0:
  print(0)
  sys.exit()
  
if x < y:
  x, y = y, x
  
k = (2*y - x)//3
print(modcomb(y-k, k))