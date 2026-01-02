import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from bisect import bisect_left

MOD = 998244353

N = int(readline())
m = map(int,read().split())
XD = sorted(zip(m,m))
X, D = zip(*XD)

class MaxSegTree():
    def __init__(self,raw_data):
        N = len(raw_data)
        self.size = 1<<(N.bit_length()) # 葉の要素数
        self.data = [0] * (2*self.size)
        self.build(raw_data)
        
    def build(self,raw_data):
        # raw_data は 0-indexed
        for i,x in enumerate(raw_data):
            self.data[self.size+i] = x
        for i in range(self.size-1,0,-1):
            x = self.data[i+i]; y = self.data[i+i+1]
            self.data[i] = x if x>y else y
    
    def update(self,i,x):
        i += self.size
        self.data[i] = x
        i >>= 1
        while i:
            x = self.data[i+i]; y = self.data[i+i+1]
            self.data[i] = x if x>y else y
            i >>= 1
    
    def get_data(self,i):
        return self.data[i+self.size]

    def get_max(self,L,R):
        # [L,R] に対する値を返す
        L += self.size
        R += self.size + 1
        # [L,R) に変更
        x = 0
        while L < R:
            if L&1:
                y = self.data[L]
                if x < y: x = y
                L += 1
                
            if R&1:
                R -= 1
                y = self.data[R]
                if x < y: x = y
            L >>= 1; R >>= 1
        return x

R = [0] + [bisect_left(X, x + d) for x,d in XD]
seg = MaxSegTree(R)

S = [0] * len(R)
for n in range(N,0,-1):
    r = R[n]
    x = seg.get_max(n, r)
    S[n] = x
    seg.update(n, x)    

dp = [0] * (N+1)
dp[0] = 1
dp_cum = [1] * (N+1)
for n,r in enumerate(S[1:],1):
    dp[r] += dp_cum[n-1]
    dp[r] %= MOD
    dp_cum[n] = dp_cum[n-1] + dp[n]
    dp_cum[n] %= MOD

print(dp_cum[-1])