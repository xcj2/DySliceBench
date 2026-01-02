N,K = map(int,input().split())
A = list(map(int,input().split()))
A = sorted(A)

mod = 10**9+7


def p(m,n):
    a = 1
    for i in range(n):
        a = a*(m-i)
    return a

def p_mod(m,n,mod):
    a = 1
    for i in range(n):
        a = a*(m-i) % mod
    return a

def c(m,n):
    return p(m,n) // p(n,n)

def c_mod(m,n,mod):
    return (p_mod(m,n,mod)*pow(p_mod(n,n,mod),mod-2,mod)) % mod

C = [0]*(N-K+1)  #C[i] = (N-i-1)C_(K-1),予め二項係数を計算しておく
for i in range(N-K+1):
    if i == 0:
        C[i] = c_mod(N-1,K-1,mod)
    else:
        C[i] = (C[i-1]*(N-K-i+1)*pow(N-i,mod-2,mod)) % mod

#各Aの元が何回max,minに採用されるかを考える

ans = 0
for i in range(N-K+1):
    ans -= (A[i]*C[i]) % mod

A.reverse()
for i in range(N-K+1):
    ans += (A[i]*C[i]) % mod

print(ans % mod)