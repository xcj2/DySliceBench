import sys
from math import gcd
from collections import Counter
MOD = 10**9 + 7
def main():
    input = sys.stdin.readline
    N = int(input())
    V = []
    z = 0
    for _ in range(N):
        A, B = map(int, input().split())
        g = gcd(A, B)
        if g == 0:
            z += 1
            continue
        A, B = A // g, B // g
        if A == 0: V.append((0, 1))
        elif A < 0: V.append((-A, -B))
        else: V.append((A, B))
    C = Counter(V)
    ans = Mint(1)
    used = set()
    for k, V in C.items():
        if k in used: continue
        a, b = k
        v = (0, 1) if b == 0 else (b, -a) if b > 0 else (-b, a)
        t = Mint(1)
        t += pow(2, V, MOD) - 1
        t += pow(2, C[v], MOD) - 1
        ans *= t
        used.add(v)
    print(ans - 1 + z)

class Mint:
    def __init__(self, value=0):
        self.value = value % MOD
        if self.value < 0: self.value += MOD

    @staticmethod
    def get_value(x): return x.value if isinstance(x, Mint) else x

    def inverse(self):
        a, b = self.value, MOD
        u, v = 1, 0
        while b:
            t = a // b
            b, a = a - t * b, b
            v, u = u - t * v, v
        if u < 0: u += MOD
        return u

    def __repr__(self): return str(self.value)
    def __eq__(self, other): return self.value == other.value
    def __neg__(self): return Mint(-self.value)
    def __hash__(self): return hash(self.value)
    def __bool__(self): return self.value != 0

    def __iadd__(self, other):
        self.value = (self.value + Mint.get_value(other)) % MOD
        return self

    def __add__(self, other):
        new_obj = Mint(self.value)
        new_obj += other
        return new_obj
    __radd__ = __add__

    def __isub__(self, other):
        self.value = (self.value - Mint.get_value(other)) % MOD
        if self.value < 0: self.value += MOD
        return self

    def __sub__(self, other):
        new_obj = Mint(self.value)
        new_obj -= other
        return new_obj

    def __rsub__(self, other):
        new_obj = Mint(Mint.get_value(other))
        new_obj -= self
        return new_obj

    def __imul__(self, other):
        self.value = self.value * Mint.get_value(other) % MOD
        return self

    def __mul__(self, other):
        new_obj = Mint(self.value)
        new_obj *= other
        return new_obj
    __rmul__ = __mul__

    def __ifloordiv__(self, other):
        other = other if isinstance(other, Mint) else Mint(other)
        self *= other.inverse()
        return self

    def __floordiv__(self, other):
        new_obj = Mint(self.value)
        new_obj //= other
        return new_obj

    def __rfloordiv__(self, other):
        new_obj = Mint(Mint.get_value(other))
        new_obj //= self
        return new_obj


if __name__ == '__main__':
    main()
