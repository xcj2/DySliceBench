import sys
readline = sys.stdin.readline

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
            pre = self.data[l+self.N0]
            for idx in (SL + SR[::-1]):
                if not check(self.segf(pre, self.data[idx])):
                    pre = self.segf(pre, self.data[idx])
                else:
                    break
            else:
                return -1
            while idx < self.N0:
                if check(self.segf(pre, self.data[2*idx])):
                    idx = 2*idx
                else:
                    pre = self.segf(pre, self.data[2*idx])
                    idx = 2*idx + 1
            return idx - self.N0

MOD = 10**9+7
def frac(limit):
    frac = [1]*limit
    for i in range(2,limit):
        frac[i] = i * frac[i-1]%MOD
    fraci = [None]*limit
    fraci[-1] = pow(frac[-1], MOD -2, MOD)
    for i in range(-2, -limit-1, -1):
        fraci[i] = fraci[i+1] * (limit + i + 1) % MOD
    return frac, fraci
frac, fraci = frac(1341398)
INF = 10**9+7
N, X, Y = map(int, readline().split())

CW = [tuple(map(int, readline().split())) for _ in range(N)]
Cw = [[] for _ in range(N)]
Cwidx = [[] for _ in range(N)]
used = set()

for i in range(N):
    c, w = CW[i]
    c -= 1
    Cw[c].append(w)
    used.add(c)
    Cwidx[c].append(i)

if len(used) == 1:
    print(1)
else:
    C, W = map(list, zip(*CW))
    minw = [INF]*N
    size = [0]*N
    T = Segtree(W, INF, initialize = True, segf = min)
    N0 = T.N0
    for col in range(N):
        if Cw[col]:
            for idx in Cwidx[col]:
                T.update(idx, INF)
            
            minv = T.query(0, N0)
            L = Cw[col]
            L.sort()
            LL = len(L)
            
            ok = -1
            ng = LL
            limit = max(X-L[0], Y-minv)
            while abs(ok-ng) > 1:
                med = (ok+ng)//2
                if L[med] <= limit:
                    ok = med
                else:
                    ng = med
            size[col] = ok+1
            minw[col] = L[0]
            for idx in Cwidx[col]:
                T.update(idx, W[idx])
    
    mw = min(W)
    minidxcol = C[W.index(mw)]-1
    candi = []
    for col in range(N):
        if mw+minw[col] <= Y or col == minidxcol:
            candi.append(size[col])
    ans = frac[sum(candi)]
    for c in candi:
        ans = ans*fraci[c]%MOD
    print(ans)
    
    