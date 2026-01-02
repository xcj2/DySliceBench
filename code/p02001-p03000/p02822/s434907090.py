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

def parorder(Edge, p):
    N = len(Edge)
    par = [0]*N
    par[p] = -1
    stack = [p]
    order = []
    visited = set([p])
    ast = stack.append
    apo = order.append
    while stack:
        vn = stack.pop()
        apo(vn)
        for vf in Edge[vn]:
            if vf in visited:
                continue
            visited.add(vf)
            par[vf] = vn
            ast(vf)
    return par, order

def getcld(p):
    res = [[] for _ in range(len(p))]
    for i, v in enumerate(p[1:], 1):
        res[v].append(i)
    return res


N = int(readline())
MOD = 10**9+7
Edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)


pow2 = [1]*(N+3)
for i in range(1, len(pow2)):
    pow2[i] = (2*pow2[i-1])%MOD
P, L = parorder(Edge, 0)

dp1 = [0]*N
dp2 = [0]*N
size = [1]*N
for l in L[:0:-1]:
    p = P[l]
    size[p] += size[l]

for l in L[:0:-1]:
    p = P[l]
    dp1[l] = (dp1[l] + pow2[size[l]-1] - 1)%MOD
    dp2[l] = (dp2[l] + pow2[size[l]-1] - 1)%MOD
    k = pow2[size[p]-1-size[l]]
    dp1[p] = (dp1[p] - (pow2[size[l]]-1) + (2*k-1)*dp2[l] + dp1[l])%MOD
    dp2[p] = (dp2[p] + 2*dp2[l]*k)%MOD

dp1[0] = (dp1[0] + pow2[size[0]-1] - 1)%MOD
print(dp1[0]*pow(pow(2, N, MOD), MOD-2, MOD)%MOD)
