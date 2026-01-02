n,blue=map(int,input().split())
red=n-blue
mod=10**9+7
framod=[1]

def framod_calc(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
        framod.append(a)

def permmod(n, k, mod):
    if n<k: return 0
    a=framod[n]
    c=framod[n-k]
    return (a * pow(c, mod-2, mod)) % mod

def combmod(n, k, mod):
    if n<k: return 0
    a=framod[n]
    b=framod[k]
    c=framod[n-k]
    return (a * pow(b, mod-2, mod) * pow(c, mod-2, mod)) % mod

framod_calc(n+1, mod)

for i in range(1, blue+1):
    x=combmod(n-blue+1,i,mod)*combmod(blue-1,i-1,mod)
    print(x%mod)