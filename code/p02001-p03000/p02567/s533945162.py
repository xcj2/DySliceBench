class segment_tree:
    __slots__ = ["op_M", "e_M","N","N0","dat"]
    def __init__(self, N, operator_M, e_M):
        self.op_M = operator_M
        self.e_M = e_M
        self.N = N
        self.N0 = 1<<(N-1).bit_length()
        self.dat = [self.e_M]*(2*self.N0)
    
    # 長さNの配列 initial で初期化
    def build(self, initial):
        self.dat[self.N0:self.N0+len(initial)] = initial[:]
        for k in range(self.N0-1,0,-1):
            self.dat[k] = self.op_M(self.dat[2*k], self.dat[2*k+1])

    # a_k の値を x に更新
    def update(self,k,x):
        k += self.N0
        self.dat[k] = x
        k >>= 1
        while k:
            self.dat[k] = self.op_M(self.dat[2*k], self.dat[2*k+1])
            k >>= 1

    # 区間[L,R]をopでまとめる
    def query(self,L,R):
        L += self.N0; R += self.N0 + 1 
        sl = sr = self.e_M
        while L < R:
            if R & 1:
                R -= 1
                sr = self.op_M(self.dat[R],sr)
            if L & 1:
                sl = self.op_M(sl,self.dat[L])
                L += 1
            L >>= 1; R >>= 1
        return self.op_M(sl,sr)

    def get(self, k): #k番目の値を取得。query[k,k]と同じ
        return self.dat[k+self.N0]
    
    """
    f(x_l*...*x_{r-1}) が True になる最大の r 
    つまり TTTTFFFF となるとき、F となる最小の添え字
    存在しない場合 n が返る
    f(e_M) = True でないと壊れる
    """
    def max_right(self,l,f):
        if l == self.N: return self.N;
        l += self.N0
        sm = self.e_M
        while True:
            while l&1==0:
                l >>= 1
            
            if not f(self.op_M(sm,self.dat[l])):
                while l < self.N0:
                    l *= 2
                    if f(self.op_M(sm,self.dat[l])):
                        sm = self.op_M(sm,self.dat[l])
                        l += 1
                return l - self.N0

            sm = self.op_M(sm,self.dat[l])
            l += 1
            if (l & -l) == l: break
        
        return self.N

    """
    f(x_l*...*x_{r-1}) が True になる最小の l
    つまり FFFFTTTT となるとき、T となる最小の添え字
    存在しない場合 r が返る
    f(e_M) = True でないと壊れる
    """
    def min_left(self,r,f):
        if r == 0: return 0
        r += self.N0
        sm = self.e_M
        
        while True:
            r -= 1
            while r > 1 and r&1:
                r >>= 1

            if not f(self.op_M(self.dat[r],sm)):
                while r < self.N0:
                    r = r*2 + 1
                    if f(self.op_M(self.dat[r],sm)):
                        sm = self.op_M(self.dat[r],sm)
                        r -= 1
                return r + 1 - self.N0

            sm = self.op_M(self.dat[r],sm)
            if (r & -r) == r: break

        return 0




        
###########################################
import sys
readline = sys.stdin.readline

n,q = map(int, readline().split())
*a, = map(int, readline().split())

seg = segment_tree(n,max,0)
seg.build(a)

for _ in range(q):
    idx,p,v = map(int, readline().split())
    if idx==1:
        seg.update(p-1,v)
    elif idx==2:
        print(seg.query(p-1,v-1))
    else:
        print(seg.max_right(p-1,lambda x: x < v)+1)
