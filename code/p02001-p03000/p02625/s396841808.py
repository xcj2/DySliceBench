import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


class ModInt:
    MOD = 10 ** 9 + 7

    def __init__(self, x):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)

    def __repr__(self):
        return str(self.x)

    def __add__(self, other):
        return (
            ModInt(self.x + other.x) if isinstance(other, ModInt) else
            ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x) if isinstance(other, ModInt) else
            ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x) if isinstance(other, ModInt) else
            ModInt(self.x * other)
        )

    def __truediv__(self, other):
        return (
            ModInt(
                self.x * pow(other.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, MOD - 2, MOD))
        )

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(self.x, other, MOD))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x) if isinstance(other, ModInt) else
            ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(
                other.x * pow(self.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(other * pow(self.x, MOD - 2, MOD))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, MOD))
        )

    def set_mod_divisor(self, divisor):
        ModInt.MOD = divisor


def comb_mod(n, r):
    res = 1
    r = min(n - r, r)

    for i in range(r):
        res *= (n - i)
        res %= MOD
        res *= pow((r - i), MOD - 2, MOD)

    return res


def main():
    n, m = map(int, readline().split())
    comb = ModInt(0)
    p1 = ModInt(1)  # mPs
    p2 = ModInt(1)  # m-sPn-s
    c1 = ModInt(1)  # nCs
    sign = -1

    for i in range(n):
        p2 *= (m - i)

    ans = p2 * p2

    for i in range(1, n + 1):
        p1 *= (m - i + 1)
        p2 *= pow(m - i + 1, MOD - 2, MOD)
        c1 *= (n - i + 1)
        c1 *= pow(i, MOD - 2, MOD)
        sign *= (-1)
        comb += p1 * p2 * p2 * c1 * sign

    ans -= comb

    print(ans)



if __name__ == '__main__':
    main()
