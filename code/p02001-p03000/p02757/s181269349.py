import sys
def main():
    input = sys.stdin.readline
    N,P = map(int, input().split())
    S = input().rstrip()
    D = list(map(int, S))
    
    ans = 0
    if P == 2:
        for i, d in enumerate(D):
            if d&1 == 0: ans += i + 1
        return ans

    if P == 5:
        for i, d in enumerate(D):
            if d == 0 or d == 5: ans += i + 1
        return ans

    A = [0] * P
    num = Mint(0, P)
    for i in range(N):
        num += Mint(D[-1-i], P) * pow(10, i, P)
        A[num.value] += 1
    for a in A:
        ans += a * (a-1) // 2
    ans += A[0]
    return ans

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
    ans = main()
    print(ans)