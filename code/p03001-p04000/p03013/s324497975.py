import sys
def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)] + [-1]
    dp = [Mint() for _ in range(N+1)]
    dp[0] = Mint(1)
    j = 0
    for i in range(1,N+1):
        if i == A[j]:
            j += 1
            continue
        dp[i] += dp[i-1]
        if i >= 2: dp[i] += dp[i-2]

    print(dp[N])

class Mint:
    def __init__(self, value=0, mod=10**9+7):
        self.value = ((value % mod) + mod) % mod
        self.mod = mod

    @staticmethod
    def get_value(x): return x.value if isinstance(x, Mint) else x

    def inverse(self):
        a, b = self.value, self.mod
        u, v = 1, 0
        while b:
            t = a // b
            b, a = a - t * b, b
            v, u = u - t * v, v
        return (u + self.mod) % self.mod

    def __repr__(self): return str(self.value)
    def __eq__(self, other): return self.value == other.value
    def __neg__(self): return Mint(-self.value, self.mod)
    def __hash__(self): return hash(self.value)
    def __bool__(self): return self.value != 0

    def __iadd__(self, other):
        self.value = (self.value + Mint.get_value(other)) % self.mod
        return self
    def __add__(self, other):
        new_obj = Mint(self.value, self.mod)
        new_obj += other
        return new_obj
    __radd__ = __add__

    def __isub__(self, other):
        self.value = (self.value - Mint.get_value(other) + self.mod) % self.mod
        return self
    def __sub__(self, other):
        new_obj = Mint(self.value, self.mod)
        new_obj -= other
        return new_obj
    def __rsub__(self, other):
        new_obj = Mint(Mint.get_value(other), self.mod)
        new_obj -= self
        return new_obj

    def __imul__(self, other):
        self.value = self.value * Mint.get_value(other) % self.mod
        return self
    def __mul__(self, other):
        new_obj = Mint(self.value, self.mod)
        new_obj *= other
        return new_obj
    __rmul__ = __mul__

    def __ifloordiv__(self, other):
        other = other if isinstance(other, Mint) else Mint(other, self.mod)
        self *= other.inverse
        return self
    def __floordiv__(self, other):
        new_obj = Mint(self.value, self.mod)
        new_obj //= other
        return new_obj
    def __rfloordiv__(self, other):
        new_obj = Mint(Mint.get_value(other), self.mod)
        new_obj //= self
        return new_obj

if __name__ == '__main__':
    main()