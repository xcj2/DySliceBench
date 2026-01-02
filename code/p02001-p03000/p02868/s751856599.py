"""
双対セグ木
アクセスは0-indexed, 内部のツリーは 1-indexed
関数は閉区間
作用素は右から作用とする

引数：
    N: 処理する区間の長さ
    compose: 作用素を合成させる関数 (max, min, __add__,ラムダ式,関数定義など)
    UNIT: 恒等作用素
    funcval(x,f) = f(x)
"""

class segment_tree_dual:
    def __init__(self, N, compose, funcval, UNIT=None):
        self.compose = compose
        self.UNIT = UNIT
        self.funcval = funcval

        self.height = (N-1).bit_length() #木の高さ
        self.N0 = 1<<self.height #木の横幅 >= N
        self.laz = [self.UNIT]*(2*self.N0) #作用素の木
        self.val = None #値の配列

    #初期値の配列を作る
    def build(self,initial):
        self.val = initial[:]

    #laz[k] を子に伝える、
    def propagate(self,k):
        if self.laz[k] == self.UNIT: return;
        if self.N0 <= k:
            self.val[k-self.N0] = self.funcval(self.val[k-self.N0], self.laz[k])
            self.laz[k] = self.UNIT
        else:
            self.laz[(k<<1)  ] = self.compose(self.laz[(k<<1)  ],self.laz[k]);
            self.laz[(k<<1)+1] = self.compose(self.laz[(k<<1)+1],self.laz[k]);
            self.laz[k] = self.UNIT;
    
    # laz[k]およびその上に位置する作用素をすべて伝播
    def thrust(self,k):
        for i in range(self.height,-1,-1): self.propagate(k>>i)
    
    def thrust_for_update(self,k):
        while k&1 == 0: k//=2
        for i in range(k.bit_length()-1,-1,-1): self.propagate(k>>i)

    # 区間[L,R]に関数 f を作用
    def update(self, L,R,f):
        """まず伝播させる（オペレータが可換なら必要ない）"""
        L += self.N0; R += self.N0+1
        self.thrust_for_update(L)
        self.thrust_for_update(R-1)
        
        #[L,R)に対応する区間たちに関数 f を合成
        while L < R:
            if R & 1:
                R -= 1
                self.laz[R] = self.compose(self.laz[R],f)
            if L & 1:
                self.laz[L] = self.compose(self.laz[L],f)
                L += 1
            L >>= 1; R >>= 1
    
    # values[k] を取得。
    def point_get(self, k):
        res = self.val[k]
        k += self.N0
        while k:
            res = self.funcval(res, self.laz[k])
            k //= 2
        return res
    
    # values[k] = x 代入する
    def point_set(self, k): 
        self.thrust(k)
        self.val[k] = x



###########################################################################
#日経2020予選D
#https://atcoder.jp/contests/nikkei2019-2-qual/submissions/8384133 (伝播あり)
#https://atcoder.jp/contests/nikkei2019-2-qual/submissions/8384138 (伝播なし)
###########################################################################

# coding: utf-8
# Your code here!
 
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline 

n,m = [int(i) for i in readline().split()]
lrc = [tuple(int(i) for i in readline().split()) for _ in range(m)]
lrc.sort()

compose = lambda f,g: min(f,g)
funcval = lambda x,f: min(x,f)
UNIT = INF = 10**18

seg = segment_tree_dual(n, compose, funcval, UNIT)
seg.build([0]+[INF]*(n-1))

for l,r,c in lrc:
    l -= 1
    r -= 1
    v = seg.point_get(l)
    seg.update(l+1,r,v+c)

ans = seg.point_get(n-1)

if ans != INF:
    print(ans)
else:
    print(-1)



