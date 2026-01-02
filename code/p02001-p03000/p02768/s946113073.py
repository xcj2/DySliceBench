import sys, math
def input():
    return sys.stdin.readline()[:-1]
from itertools import permutations, combinations
from collections import defaultdict, Counter
from math import factorial
from bisect import bisect_left # bisect_left(list, value)
#from fractions import gcd
enu = enumerate

sys.setrecursionlimit(10**7)
n, a, b = map(int, input().split())
MOD = 10**9 + 7

class ModInt:
    def __init__(self, x):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

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

def cmb(n, r, p):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = 1
    for i in range(n, n - r, -1):
        over = over * i % p
    under = 1
    for i in range(1, r + 1):
        under = under * i % p
    inv = pow(under, p - 2, p)
    return over * inv % p

cnt = pow(2, n, MOD)
ng1 = cmb(n, a, MOD)
ng2 = cmb(n, b, MOD)

cnt, ng1, ng2 = map(ModInt, [cnt, ng1, ng2])

res = (cnt - ng1 - ng2 - 1)

print(res)


