import sys

input = lambda: sys.stdin.readline().rstrip()


class SegTree:

    def __init__(self, init_val, segfunc, ide_ele):

        n = len(init_val)
        self.ide_ele = ide_ele
        self.segfunc = segfunc
        self.num = 2**(n - 1).bit_length()
        self.seg = [self.ide_ele] * 2 * self.num

        for i in range(n):
            self.seg[i + self.num - 1] = init_val[i]

        for i in range(self.num - 2, -1, -1):
            self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2])

    def update(self, k, x):
        k += self.num - 1
        self.seg[k] = x
        while k:
            k = (k - 1) // 2
            self.seg[k] = self.segfunc(self.seg[k * 2 + 1], self.seg[k * 2 + 2])

    def query(self, p, q):
        if q <= p:
            return self.ide_ele
        p += self.num - 1
        q += self.num - 2
        res = self.ide_ele
        while q - p > 1:
            if p & 1 == 0:
                res = self.segfunc(res, self.seg[p])
            if q & 1 == 1:
                res = self.segfunc(res, self.seg[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.segfunc(res, self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res, self.seg[p]), self.seg[q])
        return res


def solve():

    N = int(input())
    S = list(input())
    Q = int(input())
    seg = [[0 for _ in range(N)] for _ in range(26)]

    for i in range(N):
        al = ord(S[i]) - ord('a')
        seg[al][i] = 1

    segtree = []
    segfunc = lambda a, b: a | b

    for i in range(26):
        segtree.append(SegTree(seg[i], segfunc, 0))

    ans = []
    for i in range(Q):
        a, b, c = input().split()
        a = int(a)

        if a == 1:
            b = int(b) - 1
            ps = S[b]
            S[b] = c
            segtree[ord(ps) - ord('a')].update(b, 0)
            segtree[ord(c) - ord('a')].update(b, 1)
        elif a == 2:
            b, c = int(b) - 1, int(c)
            count = 0
            for i in range(26):
                count += segtree[i].query(b, c)
            ans.append(count)

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    solve()
