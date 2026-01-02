mod = 10**9+7

FRAC_RANGE = 2000000
frac = [1] * FRAC_RANGE

for i in range(2,FRAC_RANGE):
    frac[i] = frac[i-1] * i % mod

def combi(n,k):
    a = frac[n]
    b = modpow(frac[k],mod-2)
    c = modpow(frac[n-k],mod-2)
    return a*b*c%mod

def bi(x):
    o = []
    while x != 0:
        o.append(x%2)
        x //= 2
    return o

def modpow(m,n):
    o = bi(n)
    p = [m]
    leo = len(o)
    while leo > len(p):
        a = p[-1]
        p.append(a*a%mod)
    b = 1
    for i in range(leo):
        if o[i] == 1:
            b *= p[i]
            b %= mod
    return b

X,Y = map(int,input().split())

A = (-1) * X +   2  * Y
B =   2  * X + (-1) * Y

if A % 3 or B % 3 or A < 0 or B < 0:
    print(0)
    exit()

A //= 3
B //= 3

print(combi(A+B,min(A,B)))