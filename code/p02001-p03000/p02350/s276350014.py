from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
print = sys.stdout.write
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

class SegmentTree:
    def __init__(self,N,d):
        self.N0 = 2**(N-1).bit_length()
        self.node = [d]*(self.N0*2)
        self.lazy = [None]*(self.N0*2)

    def gindex(self,l,r):
        L = l + self.N0
        R = r + self.N0
        lm = (L // (L & -L)) >> 1
        rm = (R // (R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1; R >>= 1
        while L:
            yield L
            L >>= 1

    def propagates(self,*ids):
        for i in reversed(ids):
            v = self.lazy[i-1]
            if v is None:
                continue
            self.lazy[2*i-1] = self.lazy[2*i] = v
            self.node[2*i-1] = self.node[2*i] = v
            self.lazy[i-1] = None

    def update(self,l,r,x): #iの値をxに更新
        *ids, = self.gindex(l, r)

        # トップダウンにlazyの値を伝搬
        self.propagates(*ids)

        # 区間[l, r)のnode, lazyの値を更新
        L = self.N0 + l
        R = self.N0 + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] = self.node[R-1] = x
            if L & 1:
                self.lazy[L-1] = self.node[L-1] = x
                L += 1
            L >>= 1; R >>= 1

        # 伝搬させた区間について、ボトムアップにnodeの値を伝搬する
        for i in ids:
            self.node[i-1] = self.process(self.node[2*i-1], self.node[2*i])

    def query(self,l, r):
        # トップダウンにlazyの値を伝搬
        self.propagates(*self.gindex(l, r))
        L = self.N0 + l
        R = self.N0 + r

        # 区間[l, r)の最小値を求める
        s = INF
        while L < R:
            if R & 1:
                R -= 1
                s = self.process(s, self.node[R-1])
            if L & 1:
                s = self.process(s, self.node[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

    def process(self,x,y): #x,yが子の時，親に返る値
        return min(x,y)

N,Q = inpl()
ST = SegmentTree(N,2**31-1)
ans = []
for _ in range(Q):
    c,*arg = inpl()
    if c:
        s,t = arg
        ans.append(str(ST.query(s,t+1)))
    else:
        s,t,x = arg
        ST.update(s,t+1,x)

print('\n'.join(ans))
print('\n')

