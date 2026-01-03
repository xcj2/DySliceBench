import sys
readline = sys.stdin.readline

class Lazysegtree:
    #RUQ
    def __init__(self, A, intv, initialize = True, segf = min):
        #区間は 1-indexed で管理
        self.N = len(A)
        self.N0 = 2**(self.N-1).bit_length()
        self.intv = intv
        self.segf = segf
        self.lazy = [None]*(2*self.N0)
        if initialize:
            self.data = [intv]*self.N0 + A + [intv]*(self.N0 - self.N)
            for i in range(self.N0-1, -1, -1):
                self.data[i] = self.segf(self.data[2*i], self.data[2*i+1]) 
        else:
            self.data = [intv]*(2*self.N0)

    def _ascend(self, k):
        k = k >> 1
        c = k.bit_length()
        for j in range(c):
            idx = k >> j
            self.data[idx] = self.segf(self.data[2*idx], self.data[2*idx+1])
            
    def _descend(self, k):
        k = k >> 1
        idx = 1
        c = k.bit_length()
        for j in range(1, c+1):
            idx = k >> (c - j)
            if self.lazy[idx] is None:
                continue
            self.data[2*idx] = self.data[2*idx+1] = self.lazy[2*idx] \
            = self.lazy[2*idx+1] = self.lazy[idx] 
            self.lazy[idx] = None
            
            
    def query(self, l, r):
        L = l+self.N0
        R = r+self.N0
        self._descend(L//(L & -L))
        self._descend(R//(R & -R)-1)
        
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
    
    def update(self, l, r, x):
        L = l+self.N0
        R = r+self.N0

        Li = L//(L & -L)
        Ri = R//(R & -R)
        self._descend(Li)
        self._descend(Ri-1)
        
        while L < R :
            if R & 1:
                R -= 1
                self.data[R] = x
                self.lazy[R] = x
            if L & 1:
                self.data[L] = x
                self.lazy[L] = x
                L += 1
            L >>= 1
            R >>= 1
        
        self._ascend(Li)
        self._ascend(Ri-1)

inf = 10**19
N, A, B = map(int, readline().split())
S = [-inf] + [int(readline()) for _ in range(N)]

MOD = 10**9+7
dpa = Lazysegtree([1] + [0]*N, 0, initialize = True, segf = lambda x, y: (x+y)%MOD)
dpb = Lazysegtree([1] + [0]*N, 0, initialize = True, segf = lambda x, y: (x+y)%MOD)

for i in range(1, N+1):
    oka = 0
    ng = i
    while abs(oka-ng) > 1:
        med = (oka+ng)//2
        if S[i] - S[med] >= A:
            oka = med
        else:
            ng = med

    okb = 0
    ng = i
    while abs(okb-ng) > 1:
        med = (okb+ng)//2
        if S[i] - S[med] >= B:
            okb = med
        else:
            ng = med
    
    tb = dpa.query(0, okb+1)
    dpa.update(i-1, i, dpb.query(0, oka+1))
    dpb.update(i-1, i, tb)
    if S[i] - S[i-1] < A:
        dpa.update(0, i-1, 0)
    if S[i] - S[i-1] < B:
        dpb.update(0, i-1, 0)
print((dpa.query(0, N+1) + dpb.query(0, N+1)) % MOD)
