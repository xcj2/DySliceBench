import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

class CombTools(object):
    def __init__(self, cap: int, mod: int):
        self.cap = cap
        self.mod = mod
        self.inv = self._calc_inv()
        self.fac = self._calc_fac()
        self.fac_inv = self._calc_fac_inv()

    def _calc_inv(self):
        inv = [0, 1]
        for i in range(2, self.cap+1):
            inv.append((self.mod - (self.mod // i) * inv[self.mod % i]) % self.mod)

        return inv

    def _calc_fac(self):
        fac = [1]
        for i in range(1, self.cap+1):
            fac.append((i * fac[-1]) % self.mod)

        return fac

    def _calc_fac_inv(self):
        fac_inv = [1]
        for i in range(1, self.cap+1):
            fac_inv.append((self.inv[i] * fac_inv[-1]) % self.mod)

        return fac_inv

    def nCr(self, n: int, r: int):
        # validation
        if r > n:
            raise ValueError("n must be larger than r (n={}, r={})".format(n, r))

        # calculation
        return self.fac[n] * self.fac_inv[n-r] * self.fac_inv[r] % self.mod

x, y = li()
MOD = 10**9 + 7

ct = CombTools(10**6, MOD)
n = (x+y) // 3

if (x+y)%3 != 0:
    print(0)
elif x < n or x > 2*n:
    print(0)
else:
    print(ct.nCr((x+y) // 3, x - (x+y) // 3))