N, K = [int(p) for p in input().split(" ")]

def framod(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
    return a

def power(n, r, mod):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod

def comb(n, k, mod):
    a=framod(n, mod)
    b=framod(k, mod)
    c=framod(n-k, mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod

def nHr(n, r):
    return comb(n+r-1, r, mod)

mod = 10**9 + 7
def f(i):
    if N-K-i+1 >= 0:
        return nHr(i, K-i) * nHr(i+1, N-K-i+1) % mod
    return 0

for i in range(K):
    print(f(i+1))
