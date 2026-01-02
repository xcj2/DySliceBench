import sys
input = lambda: sys.stdin.buffer.readline()
from bisect import bisect_left, bisect_right
INF = float("inf")

class LazySegmentTree:
    INF = float("inf")

    def __init__(self, n):
        self.n = 1 << (n-1).bit_length()
        self.data = [self.INF] * (self.n*2)
        self.lazy = [None] * (self.n*2)
    
    def build(self, data):
        for i, x in enumerate(data):
            self.data[self.n+i] = x
        for i in range(self.n-1, 0, -1):
            self.data[i] = min(self.data[i*2], self.data[i*2+1])
        
    def query(self, l, r):
        if not l < r: return self.INF
        self.__propagate(self.__getidx(l, r))

        l += self.n; r += self.n 
        res = self.INF
        while l < r:
            if l & 1:
                res = min(res, self.data[l])
                l += 1
            if r & 1:
                res = min(res, self.data[r-1])
            l >>= 1; r >>= 1
        return res
    
    def update(self, l, r, x):
        if not l < r: return
        idx = self.__getidx(l, r)
        self.__propagate(idx)

        l += self.n; r += self.n 
        while l < r:
            if l & 1:
                self.data[l], self.lazy[l] = x, x
                l += 1
            if r & 1:
                self.data[r-1], self.lazy[r-1] = x, x
            l >>= 1; r >>= 1
    
        for i in idx:
            self.data[i] = min(self.data[i*2], self.data[i*2+1])

    def __getidx(self, l, r):
        l += self.n; r += self.n 
        lm = l // ((l & -l) << 1)
        rm = r // ((r & -r) << 1)
        res = []
        while l < r:
            if l <= lm: res.append(l)
            if r <= rm: res.append(r)
            l >>= 1; r >>= 1
        while l:
            res.append(l)
            l >>= 1
        return res
    
    def __propagate(self, idx):
        for i in reversed(idx):
            val = self.lazy[i]
            if val is None: continue
            self.lazy[i*2] = val; self.lazy[i*2+1] = val
            self.data[i*2] = val; self.data[i*2+1] = val
            self.lazy[i] = None

def main():
    n, q = map(int, input().split())
    query = [None] * n
    for i in range(n):
        s, t, x = map(int, input().split())
        query[i] = s-x, t-x, x
    d = [int(input()) for _ in range(q)]
    lst = LazySegmentTree(q)

    query.sort(key=lambda x: x[2], reverse=True)

    for l, r, x in query:
        lst.update(bisect_left(d, l), bisect_left(d, r), x)

    for i in range(q):
        ans = lst.query(i, i+1)
        print(-1 if ans == INF else ans)

if __name__ == "__main__":
    main()
