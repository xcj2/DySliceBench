import sys


class Bigint:

    mod = 10**9 + 7

    def __init__(self, n):
        self.n = n % self.mod

    @classmethod
    def set_mod(cls, mod):
        cls.mod = mod

    @staticmethod
    def _to_int(n):
        t = type(n)
        if t == int:
            return n
        elif t == Bigint:
            return n.n
        else:
            raise

    @staticmethod
    def _to_bigint(n):
        t = type(n)
        if t == int:
            return Bigint(n)
        elif t == Bigint:
            return n
        else:
            raise

    def __str__(self):
        return f"{self.n}"

    def __add__(self, other):
        return Bigint(self.n + self._to_int(other))

    def __iadd__(self, other):
        self.n = (self.n + self._to_int(other)) % self.mod
        return self

    def __sub__(self, other):
        return Bigint(self.n - self._to_int(other))

    def __isub__(self, other):
        self.n = (self.n - self._to_int(other)) % self.mod
        return self

    def __mul__(self, other):
        return Bigint(self.n * self._to_int(other))

    def __imul__(self, other):
        self.n = (self.n * self._to_int((other))) % self.mod
        return self

    def __pow__(self, other):
        assert type(other) == int, "power should be integer"
        #
        if other < 0:
            return self ** (other % (self.mod-1))
        ret = Bigint(1)
        now = Bigint(self.n)
        while other > 0:
            if other & 1:
                ret *= now
            other >>= 1
            now *= now
        return ret

    def __truediv__(self, other):
        return self * (self._to_bigint(other) ** (self.mod-2))

    def __itruediv__(self, other):
        self *= (self._to_bigint(other) ** (self.mod-2))
        return self


def _ia(): return map(int, sys.stdin.readline().strip().split())


def main():
    n, m, k = _ia()
    Bigint.set_mod(998244353)
    power = [Bigint(1)]
    for i in range(n-1):
        power.append(power[i] * (m-1))

    fact = Bigint(1)
    inv = [Bigint(1)] * n
    for i in range(1, n):
        fact *= i
        inv[i] = inv[i-1] * Bigint(i) ** (-1)

    ans = Bigint(0)
    for i in range(k+1):
        c = fact * inv[n-1-i] * inv[i]
        ans += (c * m * power[n-1-i])

    return ans


if __name__ == "__main__":
    print(main())
