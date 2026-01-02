n,m=map(int,input().split())
mod=10**9+7
framod=[1]
def framod_calc(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
        framod.append(a)

def permmod(n, k, mod):
    a=framod[n]
    c=framod[n-k]
    return (a * pow(c, mod-2, mod)) % mod

def combmod(n, k, mod):
    a=framod[n]
    b=framod[k]
    c=framod[n-k]
    return (a * pow(b, mod-2, mod) * pow(c, mod-2, mod)) % mod
framod_calc(m, mod)

a=combmod(m,n,mod)*framod[n]
a%=mod
b=0
for k in range(n+1):
    b+=((((-1)**k)*combmod(n,k,mod)*combmod(m-k,n-k,mod))%mod*framod[n-k])%mod
    b%=mod
print(a*b%mod)