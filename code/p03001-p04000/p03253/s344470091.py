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
 
N,M=map(int,input().split())
primes0=prime_factorize(M)
keys=list(set(primes0))
primes={}
for i in range(len(keys)):
  k=keys[i]
  primes[k]=0
  for j in range(len(primes0)):
    if primes0[j]==k:
      primes[k]+=1
 
def cmb(n, k, mod, fac, ifac): #calc nCk under mod
    if n < k or n < 0 or k < 0:
        return 0
    else: 
        k = min(k, n-k)
        return fac[n] * ifac[k] * ifac[n-k] % mod
 
def make_tables(mod, n): #Make factorial and inverse tables under mod 
    fac = [1, 1] # factorial table
    ifac = [1, 1] #factorial of inverse table
    inverse = [0, 1] #inverse
 
    for i in range(2, n+1):
        fac.append((fac[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod//i)) % mod)
        ifac.append((ifac[-1] * inverse[-1]) % mod)
    return fac, ifac
 
mod=10**9+7
fac,ifac=make_tables(mod,N*10)
ans=1
for i in range(len(keys)):
  ans*=cmb(N+primes[keys[i]]-1, primes[keys[i]], mod, fac, ifac)
  ans%=mod
print(ans)