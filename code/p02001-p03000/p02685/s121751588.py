mod = 998244353
N,M,K = map(int,input().split())
ans = 0
def color(n,m):
    return m*(pow_k(m-1, n-1))

def pow_k(x, n):
    if n == 0:
        return 1
    K = 1
    while n > 1:
        if n % 2 != 0:
            K = K * x
            x = x ** 2
            x %= mod
            n = (n - 1) // 2
        else:
            x = x ** 2
            x %= mod
            n = n // 2

    return (K * x)%mod
invs = [0] * (N + 1)
invs[1] = 1
for i in range(2, N + 1):
    invs[i] = mod - invs[mod % i] * (mod//i) % mod
mod_inv_factorials=[1]*(N+1)

for i in range(2,N+1):
    mod_inv_factorials[i] = mod_inv_factorials[i-1]*invs[i]
    mod_inv_factorials[i] %= mod

def mod_factorial(n, m):
    r = 1
    for i in range(1, n+1):
        r *= i
        r %= m
    return r

upper = mod_factorial(N-1,mod)

for i in range(K+1):
    tmp = color(N-i,M)
    ansk = (upper*mod_inv_factorials[i]*mod_inv_factorials[N-1-i]*tmp)%mod
    ans += ansk
    ans %= mod
print(ans)

    
