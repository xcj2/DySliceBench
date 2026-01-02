class SegmentTree(object):

    def __init__(self, init_array, seg_func=min, seg_func_null=10 ** 9 + 7):

        self.seg_func = seg_func
        self.seg_func_null = seg_func_null
        self.n = 1
        while self.n < len(init_array):
            self.n *= 2
        self.dat = [0] * (2 * self.n - 1)
        for i in range(len(init_array)):
            self.dat[self.n - 1 + i] = init_array[i]
        for i in range(self.n - 2, -1, -1):
            self.dat[i] = self.seg_func(self.dat[2 * i + 1], self.dat[2 * i + 2])

    def update(self, k, a):
        k += self.n - 1
        self.dat[k] = a
        while k > 0:
            k = (k - 1) // 2
            self.dat[k] = self.seg_func(self.dat[k * 2 + 1], self.dat[k * 2 + 2])

    def query(self, p, q):
        # [p, q)
        if q <= p:
            return self.seg_func_null

        p += self.n - 1
        q += self.n - 2
        res = self.seg_func_null

        while q - p > 1:
            if p & 1 == 0:
                res = self.seg_func(res, self.dat[p])
            if q & 1 == 1:
                res = self.seg_func(res, self.dat[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.seg_func(res, self.dat[p])
        else:
            res = self.seg_func(self.seg_func(res, self.dat[p]), self.dat[q])

        return res


def solve(n, k, a_list):
    seg_tree = SegmentTree([0] * 300001, seg_func=max, seg_func_null=0)
    for i in range(n):
        a = a_list[i]
        r = seg_tree.query(max(0, a - k), min(a + k + 1, 300001))
        seg_tree.update(a, r + 1)
    return seg_tree.query(0, 300001)


def main():
    n, k = map(int, input().split())
    a_list = [int(input()) for _ in range(n)]
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(10, 3, [1, 5, 4, 3, 8, 6, 9, 7, 2, 4]) == 7


if __name__ == "__main__":
    test()
    main()
