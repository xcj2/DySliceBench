n,m=map(int,input().split())
mod = 10**9+7
fac = [1]
caf = [1]

def pow(n,p):
    res=1
    while p >0:
        if p%2==0:
            n = n**2 % mod
            p //= 2
        else:
            res = res * n % mod
            p -= 1
    return res % mod

for i in range(1,2*(10**5)):
    fac.append((fac[i-1]*i)%mod)
    caf.append(pow(fac[i],mod-2))

def ncr(n,r):
    if n < r: return 0
    return fac[n]*caf[r]*caf[n-r]

import collections

fl = [1] * 10**5
fl[0] = 0
fl[1] = 0
lprime=[]
for i in range(10**5):
    if fl[i] == 1:
        lprime.append(i)
        ti = i*2
        while ti < n:
            fl[ti] = 0
            ti += i

def prime_factorize(n):
    global lprime
    a = []
    for p in lprime:
        if p * p > n:break
        while n % p == 0:
            a.append(p)
            n //= p
    if n != 1:
        a.append(n)
    return a

tres = prime_factorize(m)
ctres = collections.Counter(tres)
res = 1
for sc in ctres.values():
    res *= ncr(n+sc-1,sc)
    res %= mod
print(res)