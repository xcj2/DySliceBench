H,W,K=map(int, input().split())

MOD = 10**9+7
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

def comb(n, r):
    p, q = 1, 1
    for i in range(r):
        p = p * (n-i) % MOD
        q = q * (i+1) % MOD
    return p * pow(q, MOD-2, MOD) % MOD

p = [1]*(8+1)
p[1] = 2
p[2] = 3
for i in range(3,W+1):
    p[i] = p[i-1] + p[i-2]

def f(x):
    if x < 1: return 1
    return p[x]

dp = [[Mint() for _ in range(W+2)] for __ in range(H+1)]
dp[0][K] += 1
for r in range(H):
    for c in range(1, W+1):
        if c >= 2:
            dp[r+1][c-1] += dp[r][c] * (f(c-3) * f(W-c-1))
        dp[r+1][c] += dp[r][c] * (f(c-2) * f(W-c-1))
        if c <= W-1:
            dp[r+1][c+1] += dp[r][c] * (f(c-2) * f(W-c-2))
print(dp[H][1])
