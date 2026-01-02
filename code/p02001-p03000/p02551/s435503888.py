import sys
readline = sys.stdin.readline

class Dualsegtree:
    def __init__(self, A, intv, initialize = True):
        self.N = len(A)
        self.N0 = 2**(self.N-1).bit_length()
        self.intv = intv
        if initialize:
            self.data = [intv]*self.N0 + A + [intv]*(self.N0 - self.N)
            for i in range(self.N0-1, 0, -1):
                self.data[i] = self.segf(self.data[2*i], self.data[2*i+1]) 
        else:
            self.data = [intv]*(2*self.N0)
    
    def segf(self, a, b):
        return min(a, b)
    
    def query(self, k):
        k += self.N0
        s = self.data[k]
        while k > 0:
            k >>= 1
            s = self.segf(s, self.data[k])
        return s
    
    def update(self, l, r, x):
        L, R = l+self.N0, r+self.N0
        while L < R:
            if R & 1:
                R -= 1
                self.data[R] = x
            if L & 1:
                self.data[L] = x
                L += 1
            L >>= 1
            R >>= 1

N, Q = map(int, readline().split())
INF = 10**9+7
H, W = Dualsegtree([N-1]*(N-1), INF, initialize = True), Dualsegtree([N-1]*(N-1), INF, initialize = True)

ans = 0


mw = N
mb = N

for _ in range(Q):
    t, x = map(int, readline().split())
    x -= 1
    if t == 1:
        st = H.query(x)
        ans += st-1
        if mw > x:
            mw = x
            W.update(0, st, x)
    else:
        st = W.query(x)
        ans += st-1
        if mb > x:
            mb = x
            H.update(0, st, x)
print((N-2)*(N-2)-ans)