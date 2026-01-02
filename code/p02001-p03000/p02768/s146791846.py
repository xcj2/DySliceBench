MOD = 10 ** 9 + 7


class ModInt:

    def __init__(self, x):
        self.x = x.x if isinstance(x, ModInt) else x % MOD

    def __str__(self): return str(self.x)
    __repr__ = __str__

    def __int__(self): return self.x
    __index__ = __int__

    def __add__(self, other): return ModInt(self.x + ModInt(other).x)

    def __sub__(self, other): return ModInt(self.x - ModInt(other).x)

    def __mul__(self, other): return ModInt(self.x * ModInt(other).x)

    def __pow__(self, other): return ModInt(pow(self.x, ModInt(other).x, MOD))

    def __truediv__(self, other): return ModInt(
        self.x * pow(ModInt(other).x, MOD - 2, MOD))

    def __floordiv__(self, other): return ModInt(self.x // ModInt(other).x)

    def __radd__(self, other): return ModInt(other + self.x)

    def __rsub__(self, other): return ModInt(other - self.x)

    def __rpow__(self, other): return ModInt(pow(other, self.x, MOD))

    def __rmul__(self, other): return ModInt(other * self.x)

    def __rtruediv__(self, other): return ModInt(
        other * pow(self.x, MOD - 2, MOD))

    def __rfloordiv__(self, other): return ModInt(other // self.x)

    def __lt__(self, other): return self.x < ModInt(other).x

    def __gt__(self, other): return self.x > ModInt(other).x

    def __le__(self, other): return self.x <= ModInt(other).x

    def __ge__(self, other): return self.x >= ModInt(other).x

    def __eq__(self, other): return self.x == ModInt(other).x

    def __ne__(self, other): return self.x != ModInt(other).x


def cmb(n, r):  # nCr = n!/(n-r)!r!
    retVal = ModInt(1)
    for i in range(n-r+1, n+1):
        retVal *= i
    for i in range(2, r+1):
        retVal /= i
    return retVal


n, a, b = map(int, input().split())


def twopow(p):
    if p == 0:
        return ModInt(1)
    if p % 2 == 0:
        t = twopow(p // 2)
        return t * t
    return 2 * twopow(p - 1)


nC = [ModInt(1)]
for i in range(1, 200005):
    nC.append(nC[-1] * (n - i + 1) / i)

print((twopow(n) - nC[a] - nC[b] - 1))
# print((twopow(n) - cmb(n, a) - cmb(n, b)-1))
