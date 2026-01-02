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

class Sieve:
    # Sieve of Eratosthenes
    def __init__(self, n):
        f = [0]*(n+1)
        primes = list()
        f[0] = f[1] = -1
        for i in range(2,n+1):
            if f[i]:
                continue
            primes.append(i)
            f[i]=i
            for j in range(i*i, n+1, i):
                if not f[j]:
                    f[j] = i
        self.f = f
        self.primes = primes
    def isPrime(self, x):
        return self.f[x] == x
    def factorList(self, x):
        res = list()
        while x > 1:
            res.append(self.f[x])
            x //= self.f[x]
        return res
    def factor(self, x):
        fl = self.factorList(x)
        if len(fl) == 0:
            return list()
        res = [[fl[0], 0]]
        for p in fl:
            if res[-1][0] == p:
                res[-1][1] += 1
            else:
                res.append([p, 1])
        return res

n = int(input())
a = list(map(int, input().split()))

l = dict()

sv = Sieve(1000005)

for i in range(n):
    f = sv.factor(a[i])
    for p in f:
        try:
            l[p[0]] = max(l[p[0]], p[1])
        except:
            l[p[0]] = p[1]

lcm = mint(1)

for f,s in l.items():
    lcm *= f**s

ans=0
for i in range(n):
    ans+=lcm/a[i]

print(ans)