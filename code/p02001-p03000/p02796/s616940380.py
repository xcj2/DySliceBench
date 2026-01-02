import sys
from operator import itemgetter 
readline = sys.stdin.readline

def compress(L):
    L2 = list(set(L))
    L2.sort()
    C = {v : k for k, v in enumerate(L2)}
    return L2, C

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
            return idx
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
            return idx

N = int(readline())
XL = [tuple(map(int, readline().split())) for _ in range(N)]
LR = [(x-l, x+l) for x, l in XL]

M = 2*N+1
inf = 1<<31
S = set([-inf])
for l, r in LR:
    S.add(l)
    S.add(r)
_, Cs = compress(list(S))
LR = [(Cs[l], Cs[r]) for l, r in LR]


table = [-inf]*M
for l, r in LR:
    table[r] = max(table[r], l)
dp = Segtree([None]*M, -inf, initialize = False, segf = max)
dp.update(0, 0)
for r in range(1, M):
    if table[r] == -inf:
        continue
    l = table[r]
    k = dp.query(0, l+1)
    dp.update(r, 1+k)

print(dp.query(0, M))
