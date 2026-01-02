from collections import Counter
from operator import itemgetter
N = int(input())
D = list(map(int, input().split()))
MOD = 998244353

class Mint:
    @staticmethod
    def get_value(x): return x.value if isinstance(x, Mint) else x

    def __init__(self, val, mod=10**9+7):
        val = Mint.get_value(val)
        self.__mod = mod
        self.__val = val % self.__mod

    @property
    def value(self): return self.__val
    @property
    def inverse(self): return pow(self.__val, self.__mod - 2, self.__mod)

    def __eq__(self, other): return self.__val == other.val
    def __ne__(self, other): return self.__val != other.val

    def __neg__(self): return Mint(self.__val, self.__mod)

    def __iadd__(self, other):
        other = Mint.get_value(other)
        self.__val = (self.__val + other) % self.__mod
        return self
    def __add__(self, other):
        new = Mint(self.__value, self.__mod)
        new += other
        return new
    def __radd__(self, other): return self + other

    def __isub__(self, other):
        other = Mint.get_value(other)
        self.__val = (self.__val - other + self.__mod) % self.__mod
        return self
    def __sub__(self, other):
        new = Mint(self.__value, self.__mod)
        new -= other
        return new
    def __rsub__(self, other):
        new = Mint(Mint.get_value(other), self.__mod)
        new -= self
        return new

    def __imul__(self, other):
        other = Mint.get_value(other)
        self.__val = self.__val * other % self.__mod
        return self
    def __mul__(self, other):
        new = Mint(self.__value, self.__mod)
        new *= other
        return new
    def __rmul__(self, other): return self * other

    def __ifloordiv__(self, other):
        other = Mint(other, self.__mod)
        self *= other.inverse
        return self
    def __floordiv__(self, other):
        new = Mint(self.__value, self.__mod)
        new //= other
        return new
    def __rfloordiv__(self, other):
        new = Mint(Mint.get_value(other), self.__mod)
        new //= self
        return new

C = Counter(D)

if D[0] != 0 or C[0] != 1:
    print(0)
    exit()

ans = Mint(1, MOD)
expected = 0
for i,c in sorted(C.items(), key=itemgetter(0)):
    if i == 0: continue
    expected += 1
    if i != expected:
        print(0)
        exit()
    ans *= pow(C[i-1], c, MOD)

print(ans.value)
