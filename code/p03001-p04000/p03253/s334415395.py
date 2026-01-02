import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def modfact(n):
    fact=[1]*(n+1)
    invfact=[1]*(n+1)
    for i in range(1,n+1):
        fact[i]=i*fact[i-1]%MOD
    invfact[n]=pow(fact[n],MOD-2,MOD)
    for i in range(n-1,-1,-1):
        invfact[i]=invfact[i+1]*(i+1)%MOD
    return fact,invfact

def prime_factorization(n):
    assert(n>=2)
    factor=[]
    sqrt=int(n**.5)
    for d in range(2,sqrt+1):
        while(n%d==0):
            n//=d
            factor.append(d)
    if n!=1: factor.append(n)
    return factor

def resolve():
    from collections import Counter
    n,m=map(int,input().split())
    if(m==1):
        print(1)
        return
        
    P=prime_factorization(m)
    C=Counter(P)
    C=list(C.values())

    N=max(C)
    fact,invfact=modfact(N+n)

    ans=1
    for v in C:
        ans*=fact[v+n-1]*invfact[n-1]*invfact[v]
        ans%=MOD
    print(ans)
resolve()