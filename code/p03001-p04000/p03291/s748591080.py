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


def main():
    s = input()
    n = len(s)
    dp_t = [ModInt(0)] * (n + 1)
    dp_a = [ModInt(0)] * (n + 1)
    dp_ab = [ModInt(0)] * (n + 1)
    dp_abc = [ModInt(0)] * (n + 1)

    dp_t[0] = ModInt(1)
    dp_a[0] = ModInt(0)
    dp_ab[0] = ModInt(0)
    dp_abc[0] = ModInt(0)

    for i, char in enumerate(s, 1):
        if char == "?":
            dp_t[i] = 3 * dp_t[i - 1]
            dp_a[i] = 3 * dp_a[i - 1] + dp_t[i - 1]
            dp_ab[i] += 3 * dp_ab[i - 1] + dp_a[i - 1]
            dp_abc[i] += 3 * dp_abc[i - 1] + dp_ab[i - 1]
        else:
            dp_t[i] = dp_t[i - 1]
            dp_a[i] += dp_a[i - 1]
            dp_ab[i] += dp_ab[i - 1]
            dp_abc[i] += dp_abc[i - 1]
            if char == "A":
                dp_a[i] += dp_t[i - 1]
            if char == "B":
                dp_ab[i] += dp_a[i - 1]
            if char == "C":
                dp_abc[i] += dp_ab[i - 1]

    print(dp_abc[-1])


if __name__ == '__main__':
    main()
