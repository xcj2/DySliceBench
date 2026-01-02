n, a, b = map(int,input().split())
mod7 = 10 ** 9 + 7
def power(a,b,mod):
    p = 1
    q = a
    while b != 0:
        if b % 2 == 1:
            p = (p * q) % mod
        q = (q * q) % mod
        b = b // 2
    return p

def fact(n, mod):
    p = 1
    for i in range(1,n+1):
        p = (p * i) % mod
    return p


def combi(n,a,mod):
    inv_af = power(fact(a,mod),mod-2,mod)
    p = 1
    for i in range(a):
        p = (p * (n-i)) % mod
    return inv_af * p % mod

Answer = (power(2, n, mod7) - combi(n, a, mod7) - combi(n, b, mod7) - 1) % mod7
print(Answer)