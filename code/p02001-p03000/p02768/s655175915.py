def power(x, a):
    if a == 0:
        return 1
    elif a == 1:
        return x
    elif a % 2 == 0:
        return power(x, a//2) **2 % mod
    else:
        return power(x, a//2) **2 * x % mod

def modinv(x):
    return power(x, mod-2)

def binomial_coefficients(n, k):
    numera = 1  
    denomi = 1  

    for i in range(k):
        numera *= n-i
        numera %= mod
        denomi *= i+1
        denomi %= mod
    return numera * modinv(denomi) % mod

n,a,b=map(int,input().split())
mod=1000000007
print((pow(2,n,mod)-1-binomial_coefficients(n, a)-binomial_coefficients(n, b))%mod)