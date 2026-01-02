class SegmentTree:

    def __init__(self, ls, ide, seg_func):
        n = len(ls)
        self.num = 2 ** (n - 1).bit_length()
        self.seg_func = seg_func
        self.ide = ide
        self.tree = [self.ide] * (2 * self.num - 1)
        for i, l in enumerate(ls):
            self.tree[i + self.num - 1] = l

        for i in range(self.num - 2, -1, -1):  # 子を束ねて親を更新
            self.tree[i] = seg_func(self.tree[2 * i + 1], self.tree[2 * i + 2])

    def update(self, i, x):
        i += self.num - 1
        self.tree[i] = x
        while i:
            i = (i-1)//2
            self.tree[i] = self.seg_func(self.tree[2 * i + 1], self.tree[2 * i + 2])

    def query(self, l, r):
        if r < l:
            return ValueError('invalid index')

        l += self.num - 1
        r += self.num - 2
        res = self.ide
        while r - l > 1:  # 右から寄りながら結果を結合していくイメージ
            if l & 1 == 0:
                res = self.seg_func(res, self.tree[l])
            if r & 1 == 1:
                res = self.seg_func(res, self.tree[r])
                r -= 1
            l = l // 2  # 親の一つ右に移動
            r = (r - 1) // 2  # 親の一つ左に移動
        if l == r:
            res = self.seg_func(res, self.tree[l])
        else:
            res = self.seg_func(res, self.tree[l])
            res = self.seg_func(res, self.tree[r])
        return res


def f(a, b):
    return a | b


n = int(input())
s = [1 << (ord(r) - ord("a")) for r in input()]
q = int(input())
st = SegmentTree(s, 0, f)

for _ in range(q):
    m, i, c = input().split()

    if int(m) - 1:
        x = st.query(int(i)-1, int(c))
        print(bin(x).count("1"))
    else:
        st.update(int(i)-1, 1 << (ord(c) - ord("a")))
