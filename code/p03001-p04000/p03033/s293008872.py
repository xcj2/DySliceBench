import sys
input = sys.stdin.readline
INF = (1<<31)
from bisect import bisect_left

class LazySegmentTree():

    def __init__(self,Q):
        self.N = Q
        self.tree = [INF]*(2*self.N)
        self.lazy = [INF]*(2*self.N)
   
    def _evaluate(self,K):#Kの上の遅延配列を評価する
        H = K.bit_length() - 1
        for i in range(H,0,-1):
            h = K >> i
            if self.lazy[h] == INF:
                continue
            self.tree[h] = min(self.tree[h],self.lazy[h])
            self.lazy[h << 1] = min(self.lazy[h << 1],self.lazy[h])
            self.lazy[h << 1|1] = min(self.lazy[h << 1|1],self.lazy[h])
            self.lazy[h] = INF
    
    def _caluculate(self,K):#Kより上を計算する
        while K > 1:
            K >>= 1
            self.tree[K] = min(self.tree[K],self.tree[K<<1],self.lazy[K<<1],self.tree[K<<1|1],self.lazy[K<<1|1])

    def range_update(self,L,R,M):#[L,R)にMを作用
        L += self.N
        R += self.N
        L0 = L//(L & -L)
        R0 = R//(R & -R) - 1
        #self._evaluate(L0)
        #self._evaluate(R0)
        while L < R:
            if L&1:
                self.lazy[L] = min(self.lazy[L],M)
                L += 1
            if R&1:
                R -= 1
                self.lazy[R] = min(self.lazy[R],M)
            L >>= 1
            R >>= 1
        #print("L0 R0 {} {}\n".format(L0,R0))
        self._caluculate(L0)
        self._caluculate(R0)
    
    def range_query(self,L,R):#[L,R)を計算する
        L += self.N
        R += self.N
        L0 = L//(L & -L)
        R0 = R//(R & -R) - 1
        self._evaluate(L0)
        self._evaluate(R0)
        v = INF
        while L < R:
            if L&1:
                v = min(v,self.tree[L],self.lazy[L])
                L += 1
            if R&1:
                R -= 1
                v = min(self.tree[R],self.lazy[R],v)
            L >>= 1
            R >>= 1
        return v
    '''
    def __str__(self):
        return '\n'.join(' '.join(str(v) for v in self.tree[1<<i:1<<(i + 1)]) for i in range((2*self.N).bit_length()))
    '''
    def debug(self):
        print(self.lazy)
        print(self.tree)
    
    def __str__(self):
        for i in range(self.N):
            self.tree[i] = min(self.tree[i],self.lazy[i])
            self.lazy[i << 1] = min(self.lazy[i << 1],self.lazy[i])
            self.lazy[i << 1|1] = min(self.lazy[i << 1|1],self.lazy[i])
            self.lazy[i] = INF
        for i in range(self.N,self.N*2):
            self.tree[i] = min(self.tree[i],self.lazy[i])
        return '\n'.join(map(str,[k if k < INF else -1 for k in self.tree[self.N:]]))


N,Q = map(int,input().split())
roadwork = [tuple(map(int,input().split())) for _ in range(N)]
D = [int(input()) for _ in range(Q)]
st = LazySegmentTree(Q)

for s,t,x in roadwork:
    l = bisect_left(D,s - x)
    r = bisect_left(D,t - x)
    st.range_update(l,r,x)
print(str(st))