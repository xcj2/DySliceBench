mod = 10**9+7
X,Y = map(int,input().split())

if (2*X-Y)%3 != 0 or (2*Y-X)%3 != 0 or 2*X-Y<0 or 2*Y-X<0:
    print(0)
    exit()

x = (2*Y-X)//3
y = (2*X-Y)//3

def factorial_mod(n,mod):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
        factorial %= mod
    return factorial

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

def n_C_k(n,k,mod):
    factorial_n = factorial_mod(n,mod)
    factorial_k = factorial_mod(k,mod)
    factorial_nk = factorial_mod(n-k,mod)
    conbi=factorial_n*pow_mod(factorial_nk,mod-2)*pow_mod(factorial_k,mod-2)
    return conbi%mod

print(n_C_k(x+y,x,mod))