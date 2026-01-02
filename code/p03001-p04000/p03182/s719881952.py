"""
遅延セグメント木（区間演算、区間更新）
dat[] の要素に モノイド M をもつ
laz[] の要素に Aut(M) をもつ（ただし作用素は「右」から作用とする）
アクセスは0-indexed, 内部のツリーは 1-indexed（つまりすべての和は tree[1]）
関数は閉区間
引数：
    N: 処理する区間の長さ
    op_M = operator: モノイド演算 (max, min, __add__,ラムダ式,関数定義など)
    e_M: 単位元
    compose: 作用素を合成させる関数 (max, min, __add__,ラムダ式,関数定義など)
    funcval(x,f) = f(x) 関数適用
    ID_M: 恒等作用素
"""
""" 作用素の例：
f \mapsto min(f,-)
    compose = min
    funcval = min
    ID_M = INF = 10**18
f \mapsto max(f,-)
    compose = max
    funcval = max
    ID_M = 0
f \mapsto f (定数関数)（区間代入、最後の操作のみが影響する）
compose = lambda f,g: (f if g == ID_M else g)
funcval = lambda x,f: (x if f == ID_M else f)
ID_M = None #Noneではなく、範囲外の数にすると速くなる
"""

class lazy_segment_tree:
    def __init__(self, N, operator_M, e_M, compose, funcval, ID_M=None):
        self.compose = compose #作用素の合成（右から）
        self.ID_M = ID_M       #恒等作用素
        self.funcval = funcval #関数適用

        self.op_M = operator_M # Mの演算
        self.e_M = e_M         # Mの単位元
        ####################################
        self.height = (N-1).bit_length() #木の段数
        self.N0 = N0 = 1<<self.height #木の横幅 >= N

        self.dat = [self.e_M]*(2*N0) #データの木
        self.laz = [self.ID_M]*(2*N0) #作用素の木
        
        """
        length = [N0>>1]*N0
        for i in range(2,N0): length[i] = length[i>>1]>>1
        self.length = length #区間の長さ
        """
        
    # 長さNの配列 initial で dat を初期化
    def build(self, initial):
        self.dat[self.N0:self.N0+len(initial)] = initial[:]
        for k in range(self.N0-1,0,-1):
            self.dat[k] = self.op_M(self.dat[2*k], self.dat[2*k+1])
    
    # dat[k] に laz[k] を適用して、laz[k] を伝播
    def propagate(self,k):
        if self.laz[k] == self.ID_M: return;
        self.dat[k] = self.reflect(k)
        if self.N0 <= k:
            self.laz[k] = self.ID_M
            return
        else:
            self.laz[2*k  ] = self.compose(self.laz[2*k  ],self.laz[k])
            self.laz[2*k+1] = self.compose(self.laz[2*k+1],self.laz[k])
            self.laz[k] = self.ID_M
            return
        
    # 遅延をすべて解消する
    def propagate_all(self):
        for i in range(1,2*self.N0): self.propagate(i)
    
    # laz[k]およびその上に位置する作用素をすべて伝播
    def thrust(self,k):
        for i in range(self.height,-1,-1): self.propagate(k>>i)

    def thrust2(self,L,R):
        for i in range(self.height,0,-1):
            self.propagate(L>>i)
            if (L>>i) != R>>i:
                self.propagate(R>>i)

    # 区間[l,r]に関数 f を作用
    def update(self, l,r,f):
        l += self.N0; r += self.N0
        #まず伝播させる
        #self.thrust(l>>1); self.thrust(r>>1)
        
        #self.thrust2(l,r)
        L = l; R = r+1
        #[l.r]に対応する区間たちに関数 f を適用
        while L < R:
            if R & 1:
                R -= 1
                self.laz[R] = self.compose(self.laz[R], f)
            if L & 1:
                self.laz[L] = self.compose(self.laz[L], f)
                L += 1
            L >>= 1; R >>= 1
        # 再計算
        #self.recalc_dat(l); self.recalc_dat(r)
        self.recalc_dat2(l,r)
        
    def reflect(self,k):
        if self.laz[k] == self.ID_M: return self.dat[k]
        else: return self.funcval(self.dat[k],self.laz[k])
        
    # dat[k] を更新したときに上部を再計算
    def recalc_dat(self,k):
        k //= 2
        while k:
            self.dat[k] = self.op_M(self.funcval(self.dat[2*k],self.laz[2*k]),self.funcval(self.dat[2*k+1],self.laz[2*k+1]))
            #self.dat[k] = self.op_M(self.reflect(2*k),self.reflect(2*k+1)))
            k //= 2

    def recalc_dat2(self,l,r):
        l //= 2; r //= 2
        while l:
            #self.dat[l] = self.op_M(self.reflect(2*l),self.reflect(2*l+1))
            self.dat[l] = self.op_M(self.funcval(self.dat[2*l],self.laz[2*l]),self.funcval(self.dat[2*l+1],self.laz[2*l+1]))
            if l != r:
                #self.dat[r] = self.op_M(self.reflect(2*r),self.reflect(2*r+1))
                self.dat[r] = self.op_M(self.funcval(self.dat[2*r],self.laz[2*r]),self.funcval(self.dat[2*r+1],self.laz[2*r+1]))
            l //= 2; r //= 2

    # val[k] を取得。
    def point_get(self, k):
        k += self.N0
        res = self.dat[k]
        while k:
            if self.laz[k] != self.ID_M:
                res = self.funcval(res, self.laz[k])
            k //= 2
        return res
    
    # values[k] = x 代入する
    def point_set(self, k,x): 
        k += self.N0
        self.thrust(k)
        self.dat[k] = x
        self.recalc_dat(k)

    # 区間[L,R]をopでまとめる
    def query(self, L,R):
        L += self.N0; R += self.N0 + 1 
        self.thrust2(L,R)
        #self.thrust(L); self.thrust(R-1)
        sl = sr = self.e_M
        while L < R:
            if R & 1:
                R -= 1
                sr = self.op_M(self.reflect(R),sr)
            if L & 1:
                sl = self.op_M(sl,self.reflect(L))
                L += 1
            L >>= 1; R >>= 1
        return self.op_M(sl,sr)


###########################################################################
###########################################################################
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.buffer.readline 

n,m = [int(i) for i in readline().split()]
lra = [tuple(int(i) for i in readline().split()) for _ in range(m)]

from operator import add, itemgetter
operator_M = max
compose = add
funcval = add
ID_M = 0
e_M = -10**18

seg = lazy_segment_tree(n+1, operator_M, e_M, compose, funcval, ID_M)
seg.build([0]+[ID_M]*(n))

#seg.build([0]*n)

ans = [] 

lra.sort(key = itemgetter(1))

j = 0

"""
N0 = self.N0
self.thrust(k)
self.dat[k] = x
self.recalc_dat(k)
"""

N0 = seg.N0
for i in range(1,n+1):
    #print(seg.laz,seg.dat,i,seg.query(0,i-1))
    #seg.point_set(i,seg.query(0,i-1))
    
    seg.dat[i+N0] = seg.query(0,i-1)
    seg.recalc_dat(i+N0)
    
    while j < m and i == lra[j][1]:
        #print("hoge")
        seg.update(*lra[j])#[0],lra[j][1],lra[j][2])
        j += 1

seg.propagate_all()
print(max(seg.dat[seg.N0:seg.N0+n+1]))


#print(seg.laz,seg.dat)

