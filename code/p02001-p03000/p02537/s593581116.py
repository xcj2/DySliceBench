class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

def segfunc(x, y):
    return max(x, y)

def main():

    N, K = map(int, input().split())
    B = []
    for _ in range(N): B.append(int(input()))
    a = [0 for _ in range(max(B)+1)]
    ide_ele = 0
    seg = SegTree(a, segfunc, ide_ele)

    ans = 0
    for i in range(N):
        l = max(0, B[i]-K)
        r = min(len(a), B[i]+K)
        v = seg.query(l, r+1)
        ans = max(ans, max(1, v+1))
        seg.update(B[i], max(1, v+1))
        # print(ans)

    return ans

if __name__ == '__main__':
    print(main())