# https://atcoder.jp/contests/abc156/submissions/10277689

# コンテスト中に通せたけどmodintクラスで実装してみる
import sys
read = sys.stdin.readline


def read_ints():
    return list(map(int, read().split()))


class ModInt:
    def __init__(self, x):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other, ModInt):
            return ModInt(self.x + other.x)
        else:
            return ModInt(self.x + other)

    def __sub__(self, other):
        if isinstance(other, ModInt):
            return ModInt(self.x - other.x)
        else:
            return ModInt(self.x - other)

    def __mul__(self, other):
        if isinstance(other, ModInt):
            return ModInt(self.x * other.x)
        else:
            return ModInt(self.x * other)

    def __truediv__(self, other):
        if isinstance(other, ModInt):
            return ModInt(self.x * pow(other.x, MOD - 2, MOD))
        else:
            return ModInt(self.x * pow(other, MOD - 2, MOD))

    def __pow__(self, other):
        if isinstance(other, ModInt):
            return ModInt(pow(self.x, other.x, MOD))
        else:
            return ModInt(pow(self.x, other, MOD))

    __radd__ = __add__

    def __rsub__(self, other):  # 演算の順序が逆
        if isinstance(other, ModInt):
            return ModInt(other.x - self.x)
        else:
            return ModInt(other - self.x)

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        if isinstance(other, ModInt):
            return ModInt(other.x * pow(self.x, MOD - 2, MOD))
        else:
            return ModInt(other * pow(self.x, MOD - 2, MOD))

    def __rpow__(self, other):
        if isinstance(other, ModInt):
            return ModInt(pow(other.x, self.x, MOD))
        else:
            return ModInt(pow(other, self.x, MOD))


def combination_mod(n, r, mod):
    if r > n:
        return 0  # このような通りの数は無いため便宜上こう定義する
    r = min(r, n - r)
    nf = rf = 1
    for i in range(r):
        nf = nf * (n - i) % mod
        rf = rf * (i + 1) % mod
    return nf * pow(rf, mod - 2, mod) % mod


def combination(n, r):
    if r > n:
        return 0  # このような通りの数は無いため便宜上こう定義する
    r = min(r, n - r)
    nf = rf = ModInt(1)
    for i in range(r):
        nf = nf * (n - i)
        rf = rf * (i + 1)
    return nf / rf


# すべての通り(2^n-1)からnCa,nCbを引けば良い
MOD = 10**9 + 7
n, a, b = read_ints()
# tmp = pow(2, n, MOD) - 1
# ans = tmp - combination_mod(n, a, MOD) - combination_mod(n, b, MOD)
# print(ans % MOD)

tmp = ModInt(2)**n - 1
ans = tmp - combination(n, a) - combination(n, b)
print(ans)
