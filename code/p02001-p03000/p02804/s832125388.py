n, k = map(int, input().split())
a = list(map(int, input().split()))

mod = 10 ** 9 + 7
a.sort()

def extGCD(a, b):
    if b == 0:
        return a, 1, 0
    g, y, x = extGCD(b, a%b)
    y -= a//b * x
    return g, x, y

def moddiv(a, b):
    _, inv, _ = extGCD(b, mod)
    return (a * inv) % mod

N = 10 ** 5 + 10
fact = [0] * (N)
fact[0] = 1
for i in range(1, N):
    fact[i] = (fact[i-1] * i) % mod

def comb(a, b):
    return moddiv(moddiv(fact[a], fact[a-b]), fact[b])

def minsum(a):
    ret = 0
    for i, x in enumerate(a[:n-k+1]):
        ret += x * comb(n-i-1, k-1)
        ret %= mod
    return ret

b = [-x for x in reversed(a)]
print((-minsum(b) - minsum(a))%mod)