import sys
input = sys.stdin.buffer.readline

INF = 10**18

class SegTree:
    def __init__(self, init_val, ide_ele, segfunc):
        self.n = len(init_val)
        self.num = 2**(self.n-1).bit_length()
        self.ide_ele = ide_ele
        self.segfunc = segfunc
        self.seg = [ide_ele]*2*self.num
        # set_val
        for i in range(self.n):
            self.seg[i+self.num] = init_val[i]
        # built
        for i in range(self.num-1, 0, -1):
            self.seg[i] = self.segfunc(self.seg[2*i], self.seg[2*i+1])

    def update(self, k, x):
        k += self.num
        self.seg[k] = x
        while k:
            k = k >> 1
            self.seg[k] = self.segfunc(self.seg[2*k], self.seg[2*k+1])

    def query(self, l, r):
        if r <= l:
            return self.ide_ele
        l += self.num
        r += self.num
        res = self.ide_ele
        while l < r:
            if r & 1:
                r -= 1
                res = self.segfunc(res, self.seg[r])
            if l & 1:
                res = self.segfunc(res, self.seg[l])
                l += 1
            l = l >> 1
            r = r >> 1
        return res

def main():

    n, x = map(int,input().split())
    A = list(map(int,input().split()))

    seg = SegTree(A, INF, min)
    ans = INF
    for k in range(n):
        t = k*x
        for i in range(n):
            if k <= i:
                t += seg.query(i-k, i+1)
            else:
                t += min(seg.query(0, i+1), seg.query(n-(k-i), n))
        ans = min(t, ans)
    print(ans)

if __name__ == '__main__':
    main()