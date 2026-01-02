n=int(input())
xd=[list(map(int,input().split())) for _ in range(n)]
xd.sort(key=lambda x:x[0])
aryx=[x for x,d in xd]
mod=998244353
dp=[1]*(n+1)
#dp[n-1]=2
r=list(range(n))
r[n-1]=n-1
from bisect import bisect_left

class SegmentTree:
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, size, f=lambda x,y : max(x,y), default=0):
        self.size = 2**(size-1).bit_length() # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default]*(self.size*2) # 要素を単位元で初期化
        self.f = f

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i*2], self.dat[i*2+1])

    def query(self, l, r):
        l += self.size
        r += self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                rres = self.f(self.dat[r], rres) # モノイドでは可換律は保証されていないので演算の方向に注意
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res
st=SegmentTree(n)
for i in range(n):
    st.update(i,i)

for i in range(n):
    x,d=xd[n-1-i]
    tmp=bisect_left(aryx,x+d)
    sti=st.query(n-1-i,tmp)
    st.update(n-1-i,sti)
    dp[n-1-i]=dp[n-1-i+1]+dp[sti+1]
    dp[n-1-i]%=mod
print(dp[0])
