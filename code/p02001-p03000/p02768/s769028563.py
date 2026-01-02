MOD = 1000000007
def mod(n):         
  return n % MOD
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
def comb(n, k):
  res = 1
  for i in range(k):
    res = multiply(res, n - i) 
  for i in range(k):
    res = divide(res, i + 1)
  return mod(res)

n, a, b = map(int, input().split())
ans = modpow(2, n) - 1
resa = comb(n, a)
resb = comb(n, b)
print(mod(ans - resa - resb))