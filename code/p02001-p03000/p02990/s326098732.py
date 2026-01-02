class PERM_COMB_MOD():
    # http://drken1215.hatenablog.com/entry/2018/06/08/210000
    def __init__(self, max_n=510000, mod=10**9+7):
        self.fac = [0]*max_n
        self.finv = [0]*max_n
        self.inv = [0]*max_n
        self.fac[0] = self.fac[1] = 1
        self.finv[0] = self.finv[1] = 1
        self.inv[1] = 1
        self.max = max_n
        self.mod = mod
        self._maesyori()

    def _maesyori(self):
        for i in range(2,self.max):
            self.fac[i] = self.fac[i-1] * i % self.mod
            self.inv[i] = self.mod - self.inv[self.mod % i] * (self.mod // i) % self.mod
            self.finv[i] = self.finv[i-1] * self.inv[i] % self.mod

    def perm(self, n, k):
        if n < k : return 0
        if n < 0 or k < 0:return 0
        return self.fac[n] * self.finv[n-k] % self.mod % self.mod

    def comb(self, n, k):
        if n < k : return 0
        if n < 0 or k < 0:return 0
        return self.fac[n] * (self.finv[k] * self.finv[n-k] % self.mod) % self.mod

p = PERM_COMB_MOD()

mod = 10**9+7
n, k = map(int, input().split())
# n個をr個に分ける
def h(n, r):
    if n == 0 and r == 0:
        return 1
    return p.comb(n-1, r-1)

for i in range(1, k+1):
    blue = h(k, i)
    red = h(n-k, i-1) + 2*h(n-k, i) + h(n-k, i+1)
    ans = blue*red
    ans %= mod
    print(ans)