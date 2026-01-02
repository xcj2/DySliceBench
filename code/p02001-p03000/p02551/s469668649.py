import sys
input = sys.stdin.readline

def func(x,y):
    return min(x,y)

class LazySegmentTree():
    def __init__(self, n):
        self.lv = (n-1).bit_length()
        self.n = 2 ** self.lv
        self.arr = [2**31-1] * (2*self.n-1)
        self.lazy = [None] * (2*self.n-1)

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
            if v is None:
                continue
            self.lazy[2*i-1] = self.arr[2*i-1] = self.lazy[2*i] = self.arr[2*i] = v
            self.lazy[i-1] = None

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
                self.lazy[R-1] = self.arr[R-1] = x
            if L & 1:
                self.lazy[L-1] = self.arr[L-1] = x
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

        s = 2**31-1
        while L < R:
            if R & 1:
                R -=1
                s = func(s, self.arr[R-1])
            if L & 1:
                s = func(s, self.arr[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

def main():
    n, q = map(int, input().split())
    row = LazySegmentTree(n - 2)
    col = LazySegmentTree(n - 2)
    row.update(0, n - 3, n - 2)
    col.update(0, n - 3, n - 2)
    ans = (n - 2) ** 2
    for _ in range(q):
        que = list(map(int, input().split()))
        pos = que[1] - 2
        if que[0] == 1:
            num = row.query(pos, pos)
            ans -= num
            num2 = col.query(0, 0)
            
            if num2 > pos:
                col.update(0, num - 1, pos)
        else:
            num = col.query(pos, pos)
            ans -= num
            num2 = row.query(0, 0)
            if num2 > pos:
                row.update(0, num - 1, pos)
    print(ans)
        
main()