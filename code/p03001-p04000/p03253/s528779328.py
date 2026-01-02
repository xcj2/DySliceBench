# ABC 110 D - Factorization
def factorization(n):
    retlist = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            retlist.append(cnt)

    if temp!=1:
        retlist.append(1)

    if retlist==[]:
        retlist.append(1)

    return retlist

def factorial_mod(n, mod):
    a = 1
    for i in range(1, n + 1):
        a *= i
        a %= mod
    return a
 
def comb_mod(n, k, mod):
    if k > n or k < 0:
        return 0
    fact_n = factorial_mod(n, mod)
    fact_k = factorial_mod(k, mod)
    fact_n_k = factorial_mod(n - k, mod)
    return (fact_n * pow(fact_k, mod - 2, mod) * pow(fact_n_k, mod - 2, mod)) % mod

n,m=map(int,input().split())

if m==1:
    print(1)
    exit()
f=[]
f=factorization(m)
mod=10**9+7
ans=1
for ff in f:
    t=comb_mod(ff+n-1,ff,mod)
    ans*=t
    ans%=mod
print(ans)