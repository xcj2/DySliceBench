X, Y = map(int, input().split())
ans = 0

MOD = 10 ** 9 + 7
class modint:
    def __init__(self, x):
        self.x = x.x if isinstance(x, modint) else x % MOD
    def __str__(self): return str(self.x)
    __repr__ = __str__
    def __int__(self): return self.x
    __index__ = __int__
    def __add__(self, other): return modint(self.x + modint(other).x)
    def __sub__(self, other): return modint(self.x - modint(other).x)
    def __mul__(self, other): return modint(self.x * modint(other).x)
    def __pow__(self, other): return modint(pow(self.x, modint(other).x, MOD))
    def __floordiv__(self, other): return modint(self.x * pow(modint(other).x, MOD - 2, MOD))
    def __lt__(self, other): return self.x < modint(other).x
    def __gt__(self, other): return self.x > modint(other).x
    def __le__(self, other): return self.x <= modint(other).x
    def __ge__(self, other): return self.x >= modint(other).x
    def __eq__(self, other): return self.x == modint(other).x
    def __ne__(self, other): return self.x != modint(other).x
    def inv(self): return pow(self.x, MOD - 2, MOD)

def modC(n, r):  # nCr = n!/(n-r)!r!
    r = min(r, n - r)
    ans = modint(1)
    for i in range(n, n - r, -1):
        ans *= i
    for i in range(2, r + 1):
        ans //= i
    return ans

if (2 * Y - X) % 3 != 0 or (2 * X - Y) % 3 != 0:
    print(0)
else:
    a, b = (2 * Y - X) // 3, (2 * X - Y) // 3
    if a == 0 and b == 0:
        print(1)
    elif a < 0 or b < 0:
        print(0)
    else:
        print(modC(a + b, a))
