def framod(n,mod):
    a=1
    for i in range(1,n+1):
        a=a * i % mod
    return a

def power(n,r,mod):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod
    
def comb(n,k,mod):
    if n<0 or k<0 or n<k: return 0
    if n==0 or k==0: return 1
    a=framod(n,mod)
    b=framod(k,mod)
    c=framod(n-k,mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod

n,m=map(int, input().split())
pf={}
for i in range(2,int(m**0.5)+1):
    while m%i==0:
        pf[i]=pf.get(i,0)+1
        m//=i
if m>1:pf[m]=1

mod=10**9+7   
ans=1
for i in pf:
    ans=(ans * comb(pf[i]+n-1,pf[i],mod)) % mod
print(ans)