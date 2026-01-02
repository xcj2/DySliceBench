from collections import Counter
N,M = map(int,input().split())
def comb(n,k,p):
  """power_funcを用いて(nCk) mod p を求める"""
  from math import factorial
  if n<0 or k<0 or n<k: return 0
  if n==0 or k==0: return 1
  a = 1
  b = 1
  c = 1
  for i in range(1,n+1):
    a = (a*i)%p
  for i in range(1,k+1):
    b = (b*i)%p
  for i in range(1,n-k+1):
    c = (c*i)%p
  return (a*power_func(b,p-2,p)*power_func(c,p-2,p))%p
def power_func(a,b,p):
  """a^b mod p を求める"""
  if b==0: return 1
  if b%2==0:
    d=power_func(a,b//2,p)
    return d*d %p
  if b%2==1:
    return (a*power_func(a,b-1,p ))%p
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
mod = 10**9 + 7
num = prime_factorize(M)
numc = Counter(num)
nums = list(numc.values())
if nums:
    H = [0 for i in range(max(nums)+1)]
    for i in set(nums):
        H[i] = comb(N+i-1,i,mod)
    ans = 1
    for i in nums:
        count = H[i]
        ans = (ans*count)%mod
    print(ans)
else:
    print(1)