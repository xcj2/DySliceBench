import sys
def I(): return int(sys.stdin.readline().rstrip())
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
S = [set([a]) for a in LS2()]


def seg_func(x,y):
    return x | y

unit = set([])

class SegTree:  # モノイドに対して適用可能、Nが2冪でなくても良い
    def __init__(self,N,seg_func,unit):
        self.N = N
        self.func = seg_func
        self.unit = unit
        self.tree = [self.unit]*(2*self.N)
    def build(self,init_value):  # 初期値を[N,2N)に格納
        for i in range(self.N):
            self.tree[i+self.N] = init_value[i]
        for i in range(self.N-1,0,-1):
            self.tree[i] = self.func(self.tree[i << 1],self.tree[i << 1 | 1])
    def set_val(self,i,x):  # i番目(0-index)の値をxに変更
        i += self.N
        self.tree[i] = x
        while i > 1:
            i >>= 1
            self.tree[i] = self.func(self.tree[i << 1],self.tree[i << 1 | 1])
    def fold(self,L,R):  # [L,R)の区間取得
        L += self.N
        R += self.N
        vL = self.unit
        vR = self.unit
        while L < R:
            if L & 1:
                vL = self.func(vL,self.tree[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.func(self.tree[R],vR)
            L >>= 1
            R >>= 1
        return self.func(vL,vR)


seg = SegTree(N,seg_func,unit)
seg.build(S)

Q = I()
for i in range(Q):
    a,b,c = LS()
    if a == '1':
        b = int(b)-1
        seg.set_val(b,set([c]))
    else:
        b,c = int(b)-1,int(c)-1
        print(len(seg.fold(b,c+1)))
