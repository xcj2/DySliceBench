
def func(x,y):
    return x+y

class LazySegmentTree():
    def __init__(self, n):
        n_ = 1
        c_ = 0
        while n_ < n:
            n_ *= 2
            c_ +=1

        self.lv = c_
        self.n = n_
        self.arr = [0] * (2*self.n-1)
        self.lazy = [0] * (2*self.n-1)

    #伝播区間
    def getidx(self, l, r):
        L = (l + self.n) >> 1
        R = (r + self.n) >> 1
        lc = 0 if l & 1 else (L & -L).bit_length()
        rc = 0 if r & 1 else (R & -R).bit_length()
        for i in range(self.lv):
            if rc <= i:
                yield R
            if L < R and lc <= i:
                yield L
            L >>= 1; R >>=1

    #伝播
    def propagate(self,*ids):
        for i in reversed(ids):
            v = self.lazy[i-1]
            if v is 0:
                continue
            self.lazy[2*i-1] += v
            self.arr[2*i-1] += v
            self.lazy[2*i] += v
            self.arr[2*i] += v
            self.lazy[i-1] = 0

    #[l, r] をxで更新
    def update(self,l,r,x):
        #[l, r)に変更
        r+=1
        *ids, = self.getidx(l,r)
        self.propagate(*ids)

        L = self.n + l; R = self.n + r
        while L < R:
            if R & 1:
                R -=1
                self.lazy[R-1] += x
                self.arr[R-1] += x
            if L & 1:
                self.lazy[L-1] += x
                self.arr[L-1] += x
                L += 1
            L >>= 1; R >>= 1

        for i in ids:
            self.arr[i-1] = func(self.arr[2*i-1], self.arr[2*i])

    #[l, r]のクエリに答える
    def query(self,l,r):
        #[l, r)に変更
        r+=1
        self.propagate(*self.getidx(l,r))
        L = self.n + l; R = self.n + r

        s = 0 #初期化！！！
        while L < R:
            if R & 1:
                R -=1
                s = func(s, self.arr[R-1])
            if L & 1:
                s = func(s, self.arr[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

#0-indexed なので1-からのときは−１する
import sys
input=sys.stdin.readline
n,q=map(int,input().split())
sg=LazySegmentTree(n)
for _ in range(q):
    l=list(map(int,input().split()))
    if l[0]==0:
        c,s,t,x=l
        sg.update(s-1,t-1,x)
    else:
        c,i=l
        print(sg.query(i-1,i-1))

