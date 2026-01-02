import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


class SegTree:  # モノイドに対して適用可能、Nが2冪でなくても良い
    def __init__(self,N,seg_func,unit):
        self.N = 1 << (N-1).bit_length()
        self.func = seg_func
        self.unit = unit
        self.tree = [self.unit]*(2*self.N)

    def build(self,init_value):  # 初期値を[N,2N)に格納
        for i in range(len(init_value)):
            self.tree[i+self.N] = init_value[i]
        for i in range(self.N-1,0,-1):
            self.tree[i] = self.func(self.tree[i << 1],self.tree[i << 1 | 1])

    def set_val(self,i,x):  # i番目(0-index)の値をxに変更
        i += self.N
        self.tree[i] = x
        i >>= 1
        while i:
            self.tree[i] = self.func(self.tree[i << 1],self.tree[i << 1 | 1])
            i >>= 1

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

    def max_right(self,l,z):  # [l,r-1] で True,[l,r] で False たる r
        if l >= self.N:
            return self.N
        l += self.N
        s = self.unit
        while True:
            while l % 2 == 0:
                l >>= 1
            if not z(self.func(s,self.tree[l])):
                while l < self.N:
                    l *= 2
                    if z(self.func(s, self.tree[l])):
                        s = self.func(s, self.tree[l])
                        l += 1
                return l - self.N
            s = self.func(s, self.tree[l])
            l += 1
            if l & -l == l:
                break
        return self.N

    def min_left(self,r,z):  # [l,r-1] で True,[l-1,r-1] で False たる l
        if r <= 0:
            return 0
        r += self.N
        s = self.unit
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not z(self.func(self.tree[r], s)):
                while r < self.N:
                    r = r*2+1
                    if z(self.func(self.tree[r], s)):
                        s = self.func(self.tree[r], s)
                        r -= 1
                return r + 1 - self.N
            s = self.func(self.tree[r], s)
            if r & -r == r:
                break
        return 0


def seg_func(x,y):
    return max(x,y)

unit = 0


N,Q = MI()
A = LI()
ST = SegTree(N,seg_func,unit)

ST.build(A)

for _ in range(Q):
    t,a,b = MI()
    if t == 1:
        ST.set_val(a-1,b)
    elif t == 2:
        print(ST.fold(a-1,b))
    else:
        def z(x):
            return x < b
        print(min(ST.max_right(a-1,z),N)+1)
