import sys
readline = sys.stdin.readline
from operator import add
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
            pre = self.intv
            for idx in (SR + SL[::-1]):
                if check(self.segf(self.data[idx], pre)):
                    break
                else:
                    pre = self.segf(self.data[idx], pre)
            else:
                return -1
            while idx < self.N0:
                if check(self.segf(self.data[2*idx+1], pre)):
                    idx = 2*idx + 1
                else:
                    pre = self.segf(self.data[2*idx+1], pre)
                    idx = 2*idx
            return idx - self.N0
        else:
            pre = self.intv
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


N, Q = map(int, readline().split())
A = list(map(int, readline().split()))
INF = 10**9+7
T = Segtree(A, -INF, initialize = True, segf = max)
Ans = []
N0 = T.N0
for _ in range(Q):
    t, x, v = map(int, readline().split())
    if t == 1:
        T.update(x-1, v)
    elif t == 2:
        Ans.append(T.query(x-1, v))
    else:
        k = T.binsearch(x-1, N0, lambda x: x >= v)
        if k == -1:
            Ans.append(N+1)
        else:
            Ans.append(k+1)

print('\n'.join(map(str, Ans)))
    