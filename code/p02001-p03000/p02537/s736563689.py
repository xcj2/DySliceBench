from sys import stdin
input = stdin.readline
class LazySegmentTree():
    def __init__(self, n, init, merge_func=min, ide_ele=10 ** 18):
        self.n = (n - 1).bit_length()
        self.merge_func = merge_func
        self.ide_ele = ide_ele
        self.data = [0 for i in range(1 << (self.n + 1))]
        self.lazy = [0 for i in range(1 << (self.n + 1))]
        for i in range(n):
            self.data[2 ** self.n + i] = init[i]
        for i in range(2 ** self.n - 1, 0, -1):
            self.data[i] = self.merge_func(self.data[2 * i], self.data[2 * i + 1])

    def propagate_above(self, i):
        m = i.bit_length() - 1
        for bit in range(m, 0, -1):
            v = i >> bit
            add = self.lazy[v]
            self.lazy[v] = 0
            self.data[2 * v] += add
            self.data[2 * v + 1] += add
            self.lazy[2 * v] += add
            self.lazy[2 * v + 1] += add

    def remerge_above(self, i):
        while i:
            i >>= 1
            self.data[i] = self.merge_func(self.data[2 * i], self.data[2 * i + 1]) + self.lazy[i]

    def update(self, l, r, x):
        l += 1 << self.n
        r += 1 << self.n
        l0 = l // (l & -l)
        r0 = r // (r & -r) - 1
        while l < r:
            self.data[l] += x * (l & 1)
            self.lazy[l] += x * (l & 1)
            l += (l & 1)
            self.data[r - 1] += x * (r & 1)
            self.lazy[r - 1] += x * (r & 1)
            l >>= 1
            r >>= 1
        self.remerge_above(l0)
        self.remerge_above(r0)

    def query(self, l, r):
        l += 1 << self.n
        r += 1 << self.n
        l0 = l // (l & -l)
        r0 = r // (r & -r) - 1
        self.propagate_above(l0)
        self.propagate_above(r0)
        res = self.ide_ele
        while l < r:
            if l & 1:
                res = self.merge_func(res, self.data[l])
                l += 1
            if r & 1:
                res = self.merge_func(res, self.data[r - 1])
            l >>= 1
            r >>= 1
        return res
def solve():
    n,k = map(int,input().split())
    a = [int(inp) for inp in stdin.read().splitlines()]
    N = 300010
    cnt = [0]* N
    LST = LazySegmentTree(N,cnt,max,-1)
    res = 0
    for i in a:
        v = LST.query(max(0,i - k),min(N,i+k) + 1)
        res = max(res,v + 1)
        cur = LST.query(i,i+1)
        LST.update(i,i+1,v+1-cur)
    print(res)


if __name__ == '__main__':
    solve()