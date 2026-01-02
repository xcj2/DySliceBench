n,m=map(int, input().split())
def is_prime(N):
    is_prime=[True]*(N+1)
    is_prime[0:2]=False,False
    for i in range(int(N**0.5)+1):
        if is_prime[i]==False:
            continue
        for j in range(i*2,N+1,i):
            is_prime[j]=False
    return is_prime
def primes(N):
    prime=is_prime(N)
    return [i for i in range(N+1) if prime[i]]
def prime_factorization(n):
    ps=primes(int(n**0.5))
    r=[]
    for i,p in enumerate(ps):
        num=0
        while(True):
            x,y=divmod(n,p)
            if y!=0:
                break
            n=x
            num+=1
        if num>0:
            r.append((p,num))
    if n>1:
        r.append((n,1))
    return r
mod=10**9+7
def add(a,b):
    return (a+b)%mod
def sub(a,b):
    return (a-b)%mod
def mul(a,b):
    return ((a%mod)*(b%mod))%mod
def pow(x,y):
    if y==0:
        return 1
    elif y==1:
        return x%mod
    elif y%2==0:
        return pow(x,y//2)**2 % mod
    else:
        return pow(x,y//2)**2 * x % mod
def div(a,b):
    return mul(a,pow(b,mod-2))
def fac(n):
    a=1
    for i in range(2,n+1):
        a=mul(a,i)
    return a

f=prime_factorization(m)
ans=1
for p in f:
    ans=mul(ans,fac(p[1]+n-1))
    ans=div(ans,fac(p[1]))
    ans=div(ans,fac(n-1))
print(ans)
