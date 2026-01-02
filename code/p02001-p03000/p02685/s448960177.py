def modpow(a,n,m):
  res=1
  while n>0:
    if n&1:res=res*a%m
    a=a*a%m
    n//=2
  return res
class mod_comb_k():
  def __init__(self, MAX_N = 10**6, mod = 10**9+7):
    self.fact = [1]
    self.fact_inv = [0] * (MAX_N + 4)
    self.mod = mod
    #if MAX_N > mod:print('MAX_N > mod !')
    for i in range(MAX_N + 3):
      self.fact.append(self.fact[-1] * (i + 1) % self.mod)
    self.fact_inv[-1] = pow(self.fact[-1], self.mod - 2, self.mod)
    for i in range(MAX_N + 2, -1, -1):
      self.fact_inv[i] = self.fact_inv[i + 1] * (i + 1) % self.mod
  def comb(self, n, k):
    if n < k:
      #print('n < k !')
      return 0
    else:return self.fact[n] * self.fact_inv[k] % self.mod * self.fact_inv[n - k] % self.mod
mod=998244353
c=mod_comb_k(mod=mod)
n,m,k=map(int,input().split())
ans=0
for i in range(k+1):
  ans+=modpow(m-1,n-i-1,mod)*c.comb(n-1,i)*m%mod
  ans%=mod
print(ans)