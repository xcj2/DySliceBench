class SegmentTree:

    def __init__(self, n, op, e):
        """
        :param n: 要素数
        :param op: 二項演算
        :param e: 単位減
        """
        self.n = n
        self.op = op
        self.e = e
        self.size = 1 << (self.n - 1).bit_length()      # st[self.size + i] = array[i]
        self.tree = [self.e] * (self.size << 1)

    def built(self, array):
        """arrayを初期値とするセグメント木を構築"""
        for i in range(self.n):
            self.tree[self.size + i] = array[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.op(self.tree[i<<1], self.tree[(i<<1)|1])

    def update(self, i, x):
        """i 番目の要素を x に更新　(0-indexed) """
        i += self.size
        self.tree[i] = x
        while i > 1:
            i >>= 1
            self.tree[i] = self.op(self.tree[i<<1], self.tree[(i<<1)|1])

    def get(self, l, r):
        """ [l, r)の区間取得の結果を返す　(0-indexed) """
        l += self.size
        r += self.size
        res_l = self.e
        res_r = self.e
        while l < r:
            if l & 1:
                res_l = self.op(res_l, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res_r = self.op(self.tree[r], res_r)
            l >>= 1
            r >>= 1
        return self.op(res_l, res_r)

    def max_right(self, l, f):
        """
        以下の条件を両方満たす r を(いずれか一つ)返す
            ・r = l or f(op(a[l], a[l + 1], ..., a[r - 1])) = true
            ・r = n or f(op(a[l], a[l + 1], ..., a[r])) = false
        """
        if l == self.n: return self.n
        l += self.size
        sm = self.e
        while True:
            while l % 2 == 0: l >>= 1
            if not f(self.op(sm, self.tree[l])):
                while l < self.size:
                    l = 2 * l
                    if f(self.op(sm, self.tree[l])):
                        sm = self.op(sm, self.tree[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.tree[l])
            l += 1
            if (l & -l) == l: break
        return self.n

    def min_left(self, r, f):
        """
        以下の条件を両方満たす l を(いずれか一つ)返す
            ・l = r or f(op(a[l], a[l + 1], ..., a[r - 1])) = true
            ・l = 0 or f(op(a[l - 1], a[l], ..., a[r - 1])) = false
        """
        if r == 0: return 0
        r += self.size
        sm = self.e
        while True:
            r -= 1
            while r > 1 and (r % 2): r >>= 1
            if not f(self.op(self.tree[r], sm)):
                while r < self.size:
                    r = 2 * r + 1
                    if f(self.op(self.tree[r], sm)):
                        sm = self.op(self.tree[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.tree[r], sm)
            if (r & -r) == r: break
        return 0

    def __getitem__(self, i):
        return self.get(i,i+1)

    def __iter__(self):
        for a in self.tree[self.size:self.size+self.n]:
            yield a

    def __str__(self):
        return str(self.tree[self.size:self.size+self.n])

##################################################################################################################
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

e = 1<<60
op = lambda x, y: x if x<y else y
st = SegmentTree(N, op, e)
query = []
st.update(0,0)
for _ in range(M):
    L, R, C = map(int, input().split())
    query.append((L-1, R-1, C))
query.sort(key=lambda x:x[1])
for L, R, C in query:
    tmp = st.get(L, R) + C
    if st[R] > tmp:
        st.update(R,tmp)
print(st[N-1] if st[N-1]!=e else -1)