MOD = 998244353
def main():
    import sys
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    fu = FactorialUtils(N)
    ans = Mint()
    for i in range(K + 1):
        tmp = Mint(1)
        tmp *= fu.choose(N - 1, i)
        tmp *= M
        tmp *= pow(M - 1, N - 1 - i, MOD)
        ans += tmp
    print(ans)

class FactorialUtils:
    def __init__(self, n, mod=MOD):
        self.__mod = mod
        self.fac = [1] * (n + 1)
        self.ifac = [1] * (n + 1)
        for i in range(2, n + 1): self.fac[i] = self.fac[i - 1] * i % mod
        self.ifac[n] = pow(self.fac[n], mod - 2, mod)
        for i in range(n, 1, -1): self.ifac[i - 1] = self.ifac[i] * i % mod

    def choose(self, n, r):
        if r < 0 or r > n: return 0
        return (self.fac[n] * self.ifac[n - r] % self.__mod) * self.ifac[r] % self.__mod

    def multichoose(self, u, k):
        return (self.fac[u + k - 1] * self.ifac[u - 1] % self.__mod) * self.ifac[k] % self.__mod

class Mint:
    def __init__(self, value=0):
        self.value = value % MOD
        if self.value < 0: self.value += MOD

    @staticmethod
    def get_value(x): return x.value if isinstance(x, Mint) else x

    def inverse(self):
        a, b = self.value, MOD
        u, v = 1, 0
        while b:
            t = a // b
            b, a = a - t * b, b
            v, u = u - t * v, v
        if u < 0: u += MOD
        return u

    def __repr__(self): return str(self.value)
    def __eq__(self, other): return self.value == other.value
    def __neg__(self): return Mint(-self.value)
    def __hash__(self): return hash(self.value)
    def __bool__(self): return self.value != 0

    def __iadd__(self, other):
        self.value = (self.value + Mint.get_value(other)) % MOD
        return self

    def __add__(self, other):
        new_obj = Mint(self.value)
        new_obj += other
        return new_obj
    __radd__ = __add__

    def __isub__(self, other):
        self.value = (self.value - Mint.get_value(other)) % MOD
        if self.value < 0: self.value += MOD
        return self

    def __sub__(self, other):
        new_obj = Mint(self.value)
        new_obj -= other
        return new_obj

    def __rsub__(self, other):
        new_obj = Mint(Mint.get_value(other))
        new_obj -= self
        return new_obj

    def __imul__(self, other):
        self.value = self.value * Mint.get_value(other) % MOD
        return self

    def __mul__(self, other):
        new_obj = Mint(self.value)
        new_obj *= other
        return new_obj
    __rmul__ = __mul__

    def __ifloordiv__(self, other):
        other = other if isinstance(other, Mint) else Mint(other)
        self *= other.inverse()
        return self

    def __floordiv__(self, other):
        new_obj = Mint(self.value)
        new_obj //= other
        return new_obj

    def __rfloordiv__(self, other):
        new_obj = Mint(Mint.get_value(other))
        new_obj //= self
        return new_obj


if __name__ == '__main__':
    main()
