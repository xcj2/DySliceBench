import sys


class Bigint:

    mod = 10**9 + 7

    def __init__(self, n):
        self.n = n % self.mod

    def __str__(self):
        return str(self.n)

    def __add__(self, other):
        ot = type(other)
        if ot == Bigint:
            return Bigint(self.n+other.n)
        elif ot == int:
            return Bigint(self.n+other)
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
        return Bigint(self.n - o)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        ot = type(other)
        if ot == Bigint:
            return Bigint(self.n*other.n)
        elif ot == int:
            return Bigint(self.n*other)
        else:
            raise ValueError("Invalid type")

    def __imul__(self, other):
        return self.__mul__(other)

    def __pow__(self, other):
        assert type(other) == int, "power should be integer"
        #
        if other < 0:
            return self ** (other % (self.mod-1))
        ret = Bigint(1)
        now = Bigint(self.n)
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


def _s(): return sys.stdin.readline().strip()


def _i(): return int(sys.stdin.readline().strip())


def main():
    k = _i()
    s = _s()
    n = len(s)

    fact = [Bigint(1)] * (n+k)
    for i in range(1, n+k):
        fact[i] = fact[i-1] * i

    ifact = [None] * (n+k)
    ifact[n+k-1] = fact[n+k-1] ** (-1)
    for i in range(n+k-2, -1, -1):
        ifact[i] = ifact[i+1] * (i+1)

    p = [Bigint(1)] * (k+1)
    q = [Bigint(1)] * (k+1)
    for i in range(1, k+1):
        p[i] = p[i-1] * 25
        q[i] = q[i-1] * 26

    nf = ifact[n-1]
    ret = Bigint(0)
    for i in range(k+1):
        k_ = k - i
        n_ = n - 1 + k_
        nck = fact[n_] * ifact[k_] * nf
        ret += (nck * p[k_] * q[i])

    return ret


if __name__ == "__main__":
    print(main())
