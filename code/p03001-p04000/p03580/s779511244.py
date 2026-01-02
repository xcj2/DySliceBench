import sys
readline = sys.stdin.readline

INF = 10**9+7
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

N = int(readline())
S = [0]+list(map(int, readline().strip()))

leftone = [None]*(N+1)
left = None
for i in range(N+1):
    if S[i] == 1:
        if left is None:
            left = i
        leftone[i] = left
    else:
        left = None

T = Segtree([None]*(N+1), -INF, initialize = False)
dp = [0]*(N+1)
T.update(0, 0)
T.update(1, -1)
T.update(2, -2)
for i in range(3, N+1):
    res = dp[i-1]
    if S[i] == 1:
        if S[i-1] == 0 and S[i-2] == 1:
            left = leftone[i-2]
            res = max(res, T.query(left-1, i-2)+i-2)
        if leftone[i] > 2 and S[leftone[i]-1] == 0 and S[leftone[i]-2] == 1:
            res = max(res, dp[leftone[i]-3] + i-leftone[i]+2-1)
    dp[i] = res
    T.update(i, dp[i]-i)
print(dp[-1])