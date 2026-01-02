class SegTree:
    def __init__(self, init_val, ide_ele, seg_func):
        self.segfunc = seg_func
        n = len(init_val)
        self.num = 2**(n-1).bit_length()
        self.ide_ele = ide_ele
        self.seg=[self.ide_ele]*2*self.num
        for i in range(n):
            self.seg[i+self.num-1]=init_val[i]    
        for i in range(self.num-2,-1,-1) :
            self.seg[i]=self.segfunc(self.seg[2*i+1],self.seg[2*i+2]) 
        
    def update(self, k, x):
        k += self.num-1
        self.seg[k] = x
        # k+1ではなくkでは？
        while k+1:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[k*2+1],self.seg[k*2+2])
        
    def query(self, p, q):
        if q<=p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res=self.ide_ele
        while q-p>1:
            if p&1 == 0:
                res = self.segfunc(res,self.seg[p])
            if q&1 == 1:
                res = self.segfunc(res,self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.segfunc(res,self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res,self.seg[p]),self.seg[q])
        return res

def bsearch(mn, mx, func):
    #func(i)=False を満たす最大のi
    idx = (mx + mn)//2
    while mx-mn>1:
        if func(idx):
            idx, mx = (idx + mn)//2, idx
            continue
        idx, mn = (idx + mx)//2, idx
    return idx

import sys;input=sys.stdin.readline
mod = 998244353
N=int(input())
X = []
Y = []
for _ in range(N):
    x, d = map(int, input().split())
    X.append((x,d))
X.sort()
C = [0] * N
for i in range(N):
    x, d = X[i]
    k = bsearch(-1, N, lambda j: X[j][0] >= x+d)
    C[i] = k

st = SegTree(C, -1, max)
dp = [1]*(N+1)
for i in range(N-1, -1, -1):
    y=st.query(i, C[i]+1)
    st.update(i, y)
    dp[i] = (dp[i+1]+dp[y+1]) % mod
print(dp[0])
