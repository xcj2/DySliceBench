class Factorial():
    def __init__(self,n,mod):
        self.mod = mod
        self.factorial = [0 for _ in range(n+1)]
        self.inv = [0 for _ in range(n+1)]
        self.factorial[0] = 1
        self.inv[0] = 1
        for i in range(n):
            self.factorial[i+1] = self.factorial[i]*(i+1)%mod
        self.inv[n] = pow(self.factorial[n],mod-2,mod)
        for i in range(n)[::-1]:
            self.inv[i] = self.inv[i+1]*(i+1)%mod

    def comb(self,m,k):
        return self.factorial[m]*self.inv[k]*self.inv[m-k]%self.mod

def factorization(n):
    if n == 1: return [1]
    res = []
    x = n
    y = 2
    while y*y <= x:
        while x % y == 0:
            res.append(y)
            x //= y
        y += 1
    if x > 1: res.append(x)
    return res

from collections import Counter

MOD = 1000000007
N,M = map(int,input().split())

ans = 1

if M > 1:

    F = factorization(M)
    C = Counter(F)

    fact = Factorial(200000,MOD)

    for v in C.values():
        ans *= fact.comb(N+v-1,v)
        ans %= MOD

print(ans)