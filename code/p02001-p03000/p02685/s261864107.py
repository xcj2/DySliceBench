MOD = 998244353
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
        self.x += MOD-other.x if isinstance(other, mint) else MOD-other
        self.x -= MOD if self.x >= MOD else 0
        return self
    def __imul__(self, other):
        self.x *= other.x if isinstance(other, mint) else other
        self.x %= MOD
        return self
    def __imod__(self, other):
        self.x %= other.x if isinstance(other, mint) else other
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

class Comb():
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

cb = Comb(200005)

n,m,k = map(int, input().split())
ans= mint(0)

for i in range(k+1):
    ad = mint(m)
    ad *= pow(m-1,n-1-i,MOD)
    ad *=  cb.calc(n-1,i)
    ans += ad

print(ans)

