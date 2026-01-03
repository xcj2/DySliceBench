BIGMOD = 10**9+7

def modPow(x,n):
    ans = 1
    while n >= 1:
        if bin( n & 1)==bin(1):
            ans = (ans*x) % BIGMOD
        x = x * x % BIGMOD
        n = n>>1
    return ans % BIGMOD

def modFact(N):
    fact = []
    fact.append(1) #0! = 1
    for i in range(1,N+1):
        a = fact[i-1]*i % BIGMOD
        fact.append(a)
    return fact

def modInvFact(fact):
    invFact = []
    for i in range(1,N+2):
        a = modPow(fact[i-1],BIGMOD-2)
        invFact.append(a)
    return invFact

def modPlus(a,b):
    return (a + b) % BIGMOD

def modMinus(a,b):
    if a-b >= 0:
        return (a - b) % BIGMOD
    else:
        return (a - b + BIGMOD)
    
def modMulti(a,b):
    return a * b % BIGMOD

# fact(n),invFact(r),invFact(n-r)
def nCr(fact,invFact,n,r):
    return (fact[n] * invFact[r] * invFact[n-r] ) %BIGMOD

N,M = map(int,input().split())
fact = modFact(max(N,M))
factN = fact[N]
factM = fact[M]
ans = 0
if abs(N-M) == 0:
    ans = modMulti(factN,factM)*2 % BIGMOD
elif abs(N-M) == 1:
    ans = modMulti(factN,factM)
else:
    ans = 0
    
print(ans)