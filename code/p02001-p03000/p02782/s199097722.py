MOD = 10**9+7
class mint:
    def __init__(self, x):
        self.x = x % MOD if isinstance(x, int) else int(x) % MOD
    def __str__(self):
        return str(self.x)
    __repr__ = __str__
    def __iadd__(self, other):
        self.x += other.x if isinstance(other, mint) else other
        self.x -= MOD if self.x >= MOD else 0
        return self
    def __isub__(self, other):
        self.x -= MOD-other.x if isinstance(other, mint) else MOD-other.x
        self.x -= MOD if self.x >= MOD else 0
        return self
    def __imul__(self, other):
        self.x *= other.x if isinstance(other, mint) else other.x
        self.x %= MOD
        return self
    def __imod__(self, other):
        self.x %= other.x if isinstance(other, mint) else other.x
        self.x %= MOD
        return self
    def __add__(self, other):
        return (
            mint(self.x + other.x) if isinstance(other, mint) else
            mint(self.x + other)
        )
    def __sub__(self, other):
        return (
            mint(self.x - other.x) if isinstance(other, mint) else
            mint(self.x - other)
        )
    def __mul__(self, other):
        return (
            mint(self.x * other.x) if isinstance(other, mint) else
            mint(self.x * other)
        )
    def __mod__(self, other):
        return (
            mint(self.x % other.x) if isinstance(other, mint) else
            mint(self.x % other)
        )
    def __truediv__(self, other):
        return (
            mint(
                self.x * pow(other.x, MOD - 2, MOD)
            ) if isinstance(other, mint) else
            mint(self.x * pow(other, MOD - 2, MOD))
        )
    def __pow__(self, other):
        return (
            mint(pow(self.x, other.x, MOD)) if isinstance(other, mint) else
            mint(pow(self.x, other, MOD))
        )
    __radd__ = __add__
    def __rsub__(self, other):
        return (
            mint(other.x - self.x) if isinstance(other, mint) else
            mint(other - self.x)
        )
    __rmul__ = __mul__
    def __rmod__(self, other):
        return (
            mint(other.x % self.x) if isinstance(other, mint) else
            mint(other % self.x)
        )
    def __rtruediv__(self, other):
        return (
            mint(
                other.x * pow(self.x, MOD - 2, MOD)
            ) if isinstance(other, mint) else
            mint(other * pow(self.x, MOD - 2, MOD))
        )
    def __rpow__(self, other):
        return (
            mint(pow(other.x, self.x, MOD)) if isinstance(other, mint) else
            mint(pow(other, self.x, MOD))
        )

class comb():
    # class <mint> should be imported
    def __init__(self, n):
        self.n = n
        fact = [0]*(n+1) # 1-indexed
        ifact = [0]*(n+1) # 逆元
        fact[0] = mint(1)
        for i in range(1, n+1):
            fact[i] = fact[i-1]*i
        ifact[-1] = pow(fact[-1], MOD-2)
        for i in range(n, 0, -1):
            ifact[i-1] = ifact[i]*i
        self.fact = fact
        self.ifact = ifact
    def calc(self, n, k):
        if k<0 or k>n:
            return 0
        return self.fact[n]*self.ifact[k]*self.ifact[n-k]

r1,c1,r2,c2 = map(int, input().split())
ans=0
cb=comb(r2+c2)
acr=[1]
acc=[1]
for i in range(1,r2-r1+1):
    acr.append(acr[-1]+cb.calc(i+c2-c1-1,i))

for i in range(1,c2-c1+1):
    acc.append(acc[-1]+cb.calc(i+r2-r1-1,i))

for r in range(r1+1,r2+1):
    ans+=acr[r2-r1-(r-r1-1)]*cb.calc(c1+r, r)

for c in range(c1+1,c2+1):
    ans+=acc[c2-c1-(c-c1-1)]*cb.calc(c+r1, c)

ans+=cb.calc(c1+r1, c1)
print(ans)
