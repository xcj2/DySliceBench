N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))

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

if T[N-1] != A[0]:
    print(0)
    exit()

ans = Mint(1)
for i in range(N):
    if i==0 or i==N-1: continue
    if T[i-1] != T[i]:
        if T[i] == A[0] and A[i] != A[0]:
            print(0)
            exit()
        continue
    if A[i] != A[i+1]:
        if A[i] == A[0] and T[i] != A[0]:
            print(0)
            exit()
        continue
    ans *= min(T[i], A[i])
print(ans.value)