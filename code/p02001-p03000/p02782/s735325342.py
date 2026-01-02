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

    def h(self, n, k):
        if n == k == 0:
            return 1
        return self.comb(n+k-1, k)

PCM = PERM_COMB_MOD(3*10**6+100)
mod = 10**9+7

r1,c1,r2,c2 = map(int, input().split())

def sq(R,L):
    R+=1
    L+=1
    ret = 0
    for i in range(R):
        ret += PCM.comb(L+i, i+1)
    ret %= mod
    return ret
ans = sq(r2, c2) - sq(r2, c1-1) - sq(r1-1, c2) + sq(r1-1,c1-1)
ans %= mod
print(ans)