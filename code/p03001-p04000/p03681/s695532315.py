N, M = map(int, input().split())
if N < M:
    N, M = M, N

if N - M > 1:
    print(0)
    exit()


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
    def __eq__(self, other): return self.x == modint(other).x
    def __ne__(self, other): return self.x != modint(other).x
    def __inv__(self): return pow(self.x, MOD - 2, MOD)

def fact(n):
    r = n
    for i in range(n - 1, 1, -1):
        r *= i
    return r

fn = fact(modint(N))
fm = fact(modint(M))

if N == M:
    print(fn * fm * 2)
else:
    print(fn * fm)
