class SegmentTree:
    def __init__(self, n, init_val, ide_ele=0):
        self.num = 2 ** (n - 1).bit_length()
        self.seg = [ide_ele] * 2 * self.num
        self.ide_ele = ide_ele
        for i in range(n):
            self.seg[i + self.num - 1] = init_val[i]
        for i in range(self.num - 2, -1, -1):
            self.seg[i] = self.seg_func(self.seg[2 * i + 1], self.seg[2 * i + 2])

    def update(self, k, x):
        k += self.num - 1
        self.seg[k] = x
        while k:
            k = (k - 1) // 2
            self.seg[k] = self.seg_func(self.seg[2 * k + 1], self.seg[2 * k + 2])

    def query(self, p, q):
        if q <= p:
            return self.ide_ele
        p += self.num - 1
        q += self.num - 2
        res = self.ide_ele
        while q - p > 1:
            if p & 1 == 0:
                res = self.seg_func(res, self.seg[p])
            if q & 1 == 1:
                res = self.seg_func(res, self.seg[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.seg_func(res, self.seg[p])
        else:
            res = self.seg_func(self.seg_func(res, self.seg[p]), self.seg[q])
        return res

    def seg_func(self, x, y):
        return x + y


def p_c():
    n, q = map(int, input().split())
    s = input().replace("AC", "01")
    li = list(map(lambda x: 1 if x == "0" else 0, s))
    seg = SegmentTree(n, li)
    ans = []
    for _ in range(q):
        l, r = map(int, input().split())
        ans.append(str(seg.query(l - 1, r - 1)))
    print("\n".join(ans))
    
p_c()