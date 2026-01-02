def comb(n,k,p):
  """power_funcを用いて(nCk) mod p を求める"""
  from math import factorial
  if n<0 or k<0 or n<k: return 0
  if n==0 or k==0: return 1
  a=factorial(n) %p
  b=factorial(k) %p
  c=factorial(n-k) %p
  return (a*power_func(b,p-2,p)*power_func(c,p-2,p))%p
def power_func(a,b,p):
  """a^b mod p を求める"""
  if b==0: return 1
  if b%2==0:
    d=power_func(a,b//2,p)
    return d*d %p
  if b%2==1:
    return (a*power_func(a,b-1,p ))%p
  
def conv(w, h):
  ans = 1
  mod = 10**9+7
  ma = min(w, h)
  for i in range(ma):
    ans*=((w+h-i)%mod)
    ans%=mod
    m_inv = pow(m-i,mod-2,mod)
    ans*=m_inv
    ans%=mod
  return ans

mod = 10**9+7
n = int(input())
m = n//3
a = 0
for i in range(1, m+1):
  nokori = n-3*i
  a+=comb(nokori+i-1, i-1, mod)
  a%=mod
  
print(a)