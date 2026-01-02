# from math import gcd
import sys
input = sys.stdin.readline
n = int(input())
As = list(map(int, input().split()))

def gcd(n, m):
    # 最大公約数
    a = max(n,m)
    b = min(n,m)
    while b:
        a, b = b, a % b
    return a

class segmented_tree:
    X_unit = 1 << 30
    X_f = lambda self, a, b: gcd(a,b)
    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (2*N)
        
    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x 
        # 後ろから入れていく
        for i in range(self.N-1, 0, -1):
            self.X[i] = self.X_f(self.X[i<<1], self.X[i<<1|1])

    # 1点更新
    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i<<1],self.X[i<<1|1])
    
    # 区間取得
    def fold(self, l, r):
        l += self.N
        r += self.N
        vl = self.X[l]
        vr = self.X[r-1]
        # 外から決めていく
        while l < r:
            # print(l,r)
            if l & 1:
                vl = self.X_f(vl, self.X[l])
                l += 1
            if r & 1:
                r -= 1
                vr = self.X_f(vr, self.X[r])
            l >>= 1
            r >>= 1
        return self.X_f(vl,vr)
  
st = segmented_tree(n)
st.build(As)
mx = 0
for i in range(n):
    if i == 0:
        a = st.fold(i+1,n)
    else:
        a = st.fold(0,i)
    if i+1 < n:
        b = st.fold(i+1,n)
    else:
        b = a        
    mx = max(mx,gcd(a,b))
print(mx)