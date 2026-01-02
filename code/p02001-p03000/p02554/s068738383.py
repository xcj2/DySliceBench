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


def main():
    n = _i()
    a = Bigint(10) ** n
    b = Bigint(8) ** n
    c = Bigint(9) ** n - b
    return a - b - Bigint(2) * c


if __name__ == "__main__":
    print(main())
