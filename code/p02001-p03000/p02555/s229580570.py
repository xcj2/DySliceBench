import sys


def _i(): return int(sys.stdin.readline().strip())


class Bigint:
    def __init__(self, n, mod=10**9+7):
        self.n = n % mod
        self.mod = mod
        return

    def __str__(self):
        return str(self.n)

    def __add__(self, other):
        ot = type(other)
        if ot == Bigint:
            return Bigint(self.n+other.n, self.mod)
        elif ot == int:
            return Bigint(self.n+other, self.mod)
        else:
            raise ValueError("Invalid type")

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        ot = type(other)
        if ot == Bigint:
            o = other.n
        elif ot == int:
            o = other
        else:
            raise ValueError("Invalid type")
        #
        return Bigint(self.n - o, self.mod)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        ot = type(other)
        if ot == Bigint:
            return Bigint(self.n*other.n, self.mod)
        elif ot == int:
            return Bigint(self.n*other, self.mod)
        else:
            raise ValueError("Invalid type")

    def __imul__(self, other):
        return self.__mul__(other)

    def __pow__(self, other):
        assert type(other) == int, "power should be integer"
        #
        if other < 0:
            return self ** (other % (self.mod-1))
        ret = Bigint(1, self.mod)
        now = Bigint(self.n, self.mod)
        while other > 0:
            if other % 2 == 0:
                pass
            else:
                ret *= now
            other //= 2
            now *= now
        return ret

    def __truediv__(self, other):
        ot = type(other)
        if ot == Bigint:
            o = other
        elif ot == int:
            o = Bigint(other)
        else:
            raise ValueError("Invalid type")

        self *= (o ** (o.mod-2))
        return self

    def __itruediv__(self, other):
        return self.__truediv__(other)


def factorial(n):
    fact = [Bigint(1)]
    for i in range(n):
        fact.append(fact[i]*(i+1))
    return fact


def i_factorial(n, nf):
    ifact = [None] * (n+1)
    ifact[n] = nf
    for i in range(n-1, -1, -1):
        ifact[i] = ifact[i+1] * (i+1)
    return ifact


def main():
    n = _i()
    fact = factorial(n)
    ifact = i_factorial(n, fact[-1]**-1)

    cnt = Bigint(0)
    for bou in range(n//3):
        maru = n - 3 * (bou+1)
        tot = maru + bou
        cnt += (fact[tot] * ifact[maru] * ifact[bou])
    return cnt


if __name__ == "__main__":
    print(main())
