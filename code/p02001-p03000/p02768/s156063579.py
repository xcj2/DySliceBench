class cmb():
    def __init__(self, p=10**9+7, N=10**5+1):
        self.p = p
        self.N = N
        self.fact = [1, 1]
        self.factinv = [1, 1]
        inv = [0, 1]
        for i in range(2, self.N+1):
            self.fact.append((self.fact[-1] * i) % p)
            inv.append((-inv[p%i] * (p//i)) % p)
            self.factinv.append((self.factinv[-1] * inv[-1]) % p)
    def run1(self, a, b):
        return (self.fact[a+b] * self.factinv[a] * self.factinv[b]) % self.p
    def run2(self, n, r):
        return (self.fact[n] * self.factinv[r] * self.factinv[n-r]) % self.p
mod = 10**9+7
def fur(n, r):
    p,q = 1,1
    for i in range(r):
        p = p*(n-i)%mod
        q = q*(i+1)%mod
    return p*pow(q,mod-2,mod)%mod
n, a, b = map(int, input().split())
c = cmb()
work = pow(2, n, 10**9+7)
result = (work - fur(n, a) - fur(n, b) - 1) % (10**9+7)
print(result)