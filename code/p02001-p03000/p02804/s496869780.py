N,K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()


def pow_mod(x,n):
    if n==0:
        return 1
    
    K = 1
    while n>1:
        if n%2 != 0:
            K *= x
            K %= mod
        x *= x
        x %= mod
        n //= 2

    return K*x

def factorial(n,mod):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
        factorial %= mod
    return factorial

def n_C_k(n,k,mod):
    factorial_n = factorial(n,mod)
    factorial_k = factorial(k,mod)
    factorial_nk = factorial(n-k,mod)
    conbi=factorial_n*pow_mod(factorial_nk,mod-2)*pow_mod(factorial_k,mod-2)
    return conbi%mod

ans=0
mod = 10**9+7
factorial_N = factorial(N,mod)

for i in range(N-K+1):
    if i==0:
        conbi = n_C_k(N-1,K-1,mod)
    else:
        conbi *= (N-K-i+1)*pow_mod(N-i,mod-2)
        conbi %= mod
    ans += (A[N-1-i]-A[i])*conbi
    ans %= mod

print(ans)

