n,a,b = map(int,input().split())
mod = 10**9 + 7

def bi(x):
    o = []
    while x != 0:
        o.append(x%2)
        x //= 2
    return o

def modpow(m,n):
    o = bi(n)
    leo = len(o)
    p = [m]*leo
    for i in range(1,leo):
        a = p[i-1]
        a *= a
        a %= mod
        p[i] = a
    b = 1
    for i in range(leo):
        if o[i] != 1:
            continue
        b *= p[i]
        b %= mod
    return b

def combi(a,b):
    aa = a
    mom = 1
    child = 1
    for _ in range(1,b+1):
        mom *= aa
        aa -= 1
        mom %= mod
        child *= _
        child %= mod
    return mom * modpow(child,mod-2) % mod

print((modpow(2,n)-combi(n,a)-combi(n,b)-1)%mod)