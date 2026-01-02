import sys
input = sys.stdin.readline
def MI():
    return map(int, input().split())

class segtree:
    # 1-indexed セグ木
    x_unit=0 # 単位元
    x_func=max  # 関数
    condition=lambda self,a,b:a>=b # max_right用に定義
    def __init__(self,n,seq): # 元のseqと要素数n
        self.n=n
        self.x=[self.x_unit]*(2*n)
        for i,j in enumerate(seq, self.n): # n番目からseqをx配列に移していく
            self.x[i] = j
        for i in range(self.n-1, 0, -1):
            self.x[i] = self.x_func(self.x[i*2], self.x[i*2+1])
    def update(self,i,j): # 1点更新
        i += self.n
        self.x[i]=j
        while i>1:
            i//=2 # 更新後、木の上へと登っていくついでに更新
            self.x[i]=self.x_func(self.x[i*2], self.x[i*2+1])
    def get(self, i): # 値を入手
        return self.x[i+self.n] 
    def fold(self,l,r): # 区間[l, r)の最小値などを取得 
        l+=self.n
        r+=self.n
        val_l=self.x_unit
        val_r=self.x_unit
        while l<r:
            if l & 1: # lが奇数
                val_l=self.x_func(val_l,self.x[l])
                l+=1 # 偶数に調節
            if r & 1: # rが奇数
                r-=1 # 開区間なので1個前は偶数番目の要素
                val_r=self.x_func(val_r,self.x[r])
            l //= 2
            r //= 2
        return self.x_func(val_l,val_r)
    def max_right(self, l, v): 
        # index lを含めて右にある値の中でa[j]>=vを満たす最小のindexを求める
        # 存在しない場合はnを出力
        r=self.n
        if self.condition(self.fold(l, r),v)==False:
            return r
        else:
            while r-l>1:
                l1=l
                r1=l+(r-l)//2
                l2=l+(r-l)//2
                r2=r
                if self.condition(self.fold(l1, r1),v)==True:
                    l=l1
                    r=r1
                else:
                    l=l2
                    r=r2
            return l
    def min_left(self, r, v): 
        # index rを含まずに左にある値の中でa[j]>=vを満たす最大のindexを求める
        # 存在しない場合は0を出力
        l=0
        if self.condition(self.fold(l, r),v)==False:
            return l
        else:
            while r-l>1:
                l1=l
                r1=l+(r-l)//2
                l2=l+(r-l)//2
                r2=r
                if self.condition(self.fold(l1, r1),v)==True:
                    l=l1
                    r=r1
                else:
                    l=l2
                    r=r2
            return r

n,k=MI()
seq=[0 for _ in range(300001)]
seg=segtree(300001,seq)
for i in range(n):
    a=int(input())
    left=seg.fold(max(a-k,0), a+1)
    right=seg.fold(a, min(a+k,300000)+1)
    seg.update(a,max(left,right)+1)
print(seg.fold(0, 300001))