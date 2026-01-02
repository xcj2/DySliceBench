from math import ceil, log2
import sys
z=sys.stdin.readline


# SegTreeの関数
def segfunc(x, y):
    return max(x, y)


# 単位元
# min->inf, max->-inf, add->0, mul->1
ide_ele = -1


# セグメント木
class SegTree:

    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセットする
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築
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


n, k = map(int, z().split())
a = [int(z()) for _ in range(n)]
M=300001
st = SegTree([0]*M, max, 0)
res = 0
for i in a:
    min_a = max(i-k, 0)
    max_a = min(i+k, M)
    s = st.query(min_a, max_a+1)
    st.update(i, max(s, 0)+1)
    res = max(res, max(s, 0) + 1)

print(res)
