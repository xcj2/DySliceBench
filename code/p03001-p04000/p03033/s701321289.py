#! /usr/bin/env python3
import bisect
import sys
sys.setrecursionlimit(10**9)



# Ref: https://qiita.com/takayg1/items/b7b3f7d458915bcc7a4e
class LazySegTree:
    def __init__(self, init_val, segfunc, ide_ele = 2**31 - 1):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.data = [ide_ele] * 2 * self.num
        self.lazy = [None] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.data[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])



    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            self.data[2 * i] = v
            self.data[2 * i + 1] = v
            self.lazy[i] = None

    def update(self, l, r, x): # [l, r)
        *ids, = self.gindex(l, r)
        self.propagates(*ids)
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.data[l] = x
                l += 1
            if r & 1:
                self.lazy[r - 1] = x
                self.data[r - 1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])


    def query(self, l, r): # [l, r)
        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.data[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.data[r - 1])
            l >>= 1
            r >>= 1
        return res

    def gindex(self, l, r):
        l += self.num
        r += self.num
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()

        while r > l:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1

def zarts(D,x): # 座標圧縮
    return bisect.bisect_left(D,x)
    

INF=10**20
def solve(N: int, Q: int, S: "List[int]", T: "List[int]", X: "List[int]", D: "List[int]"):

    def segfunc(x,y):
        return min(x,y)

    v = [INF] * (Q+1)

    seg = LazySegTree(v,segfunc,ide_ele=INF)

    _X = list(enumerate(X))
    _X.sort(key=lambda x:x[1],reverse=True)
    for i,x in _X:
        l = zarts(D,S[i]-X[i])
        r = zarts(D,T[i]-X[i])
        
        if l == r: continue
        seg.update(l,r,X[i])
    

    for q in range(Q):
        d = q
        # print("d",d)
        x = seg.query(d,d+1)
        if x == INF:
            x = -1

        print(x)
    
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    S = [int()] * (N)  # type: "List[int]"
    T = [int()] * (N)  # type: "List[int]"
    X = [int()] * (N)  # type: "List[int]"
    # X = [(int(),int())] * (N)  # type: "List[int]"
    for i in range(N):
        S[i] = int(next(tokens))
        T[i] = int(next(tokens))
        X[i] = int(next(tokens))
        # X[i] = (-1 * int(next(tokens)),i)
    D = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, Q, S, T, X, D)



if __name__ == "__main__":
    main()
