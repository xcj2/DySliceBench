import sys
readline = sys.stdin.readline
MOD = 998244353

class Segtree:
    def __init__(self, A, intv, initialize = True, segf = max):
        self.N = len(A)
        self.N0 = 2**(self.N-1).bit_length()
        self.intv = intv
        self.segf = segf
        if initialize:
            self.data = [intv]*self.N0 + A + [intv]*(self.N0 - self.N)
            for i in range(self.N0-1, 0, -1):
                self.data[i] = self.segf(self.data[2*i], self.data[2*i+1]) 
        else:
            self.data = [intv]*(2*self.N0)
        
    def update(self, k, x):
        k += self.N0
        self.data[k] = x
        while k > 0 :
            k = k >> 1
            self.data[k] = self.segf(self.data[2*k], self.data[2*k+1])
    
    def query(self, l, r):
        L, R = l+self.N0, r+self.N0
        s = self.intv
        while L < R:
            if R & 1:
                R -= 1
                s = self.segf(s, self.data[R])
            if L & 1:
                s = self.segf(s, self.data[L])
                L += 1
            L >>= 1
            R >>= 1
        return s
    
    def binsearch(self, l, r, check, reverse = False):
        L, R = l+self.N0, r+self.N0
        SL, SR = [], []
        while L < R:
            if R & 1:
                R -= 1
                SR.append(R)
            if L & 1:
                SL.append(L)
                L += 1
            L >>= 1
            R >>= 1
        
        if reverse:
            for idx in (SR + SL[::-1]):
                if check(self.data[idx]):
                    break
            else:
                return -1
            while idx < self.N0:
                if check(self.data[2*idx+1]):
                    idx = 2*idx + 1
                else:
                    idx = 2*idx
            return idx - self.N0
        else:
            for idx in (SL + SR[::-1]):
                if check(self.data[idx]):
                    break
            else:
                return -1
            while idx < self.N0:
                if check(self.data[2*idx]):
                    idx = 2*idx
                else:
                    idx = 2*idx + 1
            return idx - self.N0

N = int(readline())
XD = [tuple(map(int, readline().split())) for _ in range(N)]
XD.sort(key = lambda x: (x[0], -x[1]))

sXD = []
seen = set()
for x, d in XD:
    if x not in seen:
        sXD.append((x, d))
        seen.add(x)

N = len(sXD)
table = list(range(N))
T = Segtree(table, -1, initialize = True, segf = max)
X, D = map(list, zip(*sXD))
for i in range(N-1, -1, -1):
    ok = i
    ng = N
    gi = X[i] + D[i]
    while abs(ok-ng) > 1:
        med = (ok+ng)//2
        if X[med] < gi:
            ok = med
        else:
            ng = med
    table[i] = T.query(i, ok+1)
    T.update(i, table[i])

dp = [0]*(N+1)
dp[N] = 1
Dp = dp[:]
for i in range(N-1, -1, -1):
    dp[i] = Dp[table[i]+1]
    Dp[i] = (Dp[i+1] + dp[i])%MOD
print(Dp[0])