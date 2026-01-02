n = int(input())
if n<2:
    print(0)
    exit()
k=2
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
ans=0

for i in range(2, n+1):
    ans+=(combmod(n,i,mod)*(pow(2, i, mod)-2))*pow(8, n-i, mod)
    ans%=mod

print(ans)