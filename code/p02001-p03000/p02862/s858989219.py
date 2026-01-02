def factorial(N,MOD,r=True):
    fact = [1]*(N+1)
    rfact = [1]*(N+1)
    r = 1
    for i in range(1,N+1):
        fact[i] = r = r * i % MOD
    rfact[N] = r = pow(fact[N],MOD-2,MOD)
    for i in range(N, 0, -1):
        rfact[i-1] = r = r * i % MOD
    if r:
        return fact,rfact
    else:
        return fact
mod = 10**9 + 7
fact,rfact = factorial(10**6,mod)

def perm(n,k): #上のfactorialと併用
    return fact[n]*rfact[n-k]%mod
def comb(n,k): #上のfactorialと併用
    return fact[n]*rfact[k]*rfact[n-k]%mod

x,y = map(int,input().split())
if (x+y)%3:
    print(0)
    exit()
a = (-x+2*y)//3
b = (2*x-y)//3

print(comb(a+b,a) if a >= 0 and b >= 0 else 0)