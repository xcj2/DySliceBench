def framod(n, mod, a=1):
    for i in range(1,n+1):
        a= (a * i) % mod
    return a

def power(n, r, mod):
    if r == 0: return 1
    if r%2 == 0:
        return power((n*n) % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod

def comb(n, k, mod):
  a=framod(n, mod)
  b=framod(k, mod)
  c=framod(n-k, mod)
  return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod


N,K = map(int, input().split())
mod = 10**9+7

for i in range(1,K+1):
  B = K
  R = (N-K)

  if ((B-1) < (i-1)):
    print(0)
  elif ((R+1) < i):
    print(0)
  else:
    print((comb(B-1, i-1, mod) * comb(R+1, i, mod)) % mod)
