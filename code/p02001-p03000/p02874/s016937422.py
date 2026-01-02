from operator import itemgetter

class SegTree:  # 0-index !!!
    """
    fx: モノイドXでの二項演算
    ex: モノイドXでの単位元
    init(seq, fx, ex): 配列seqで初期化 O(N)
    update(i, x): i番目の値をxに更新 O(logN)
    query(l, r): 区間[l,r)をfxしたものを返す O(logN)
    get(i): i番目の値を返す
    show(): 配列を返す
    """

    def __init__(self, seq, fx, ex):
        self.n = len(seq)
        self.fx = fx
        self.ex = ex
        self.size = 1<<(self.n - 1).bit_length()
        self.tree = [ex] * (self.size * 2)
        # build
        for i, x in enumerate(seq, start=self.size):
            self.tree[i] = x
        for i in reversed(range(1, self.size)):
            self.tree[i] = self.fx(self.tree[2 * i], self.tree[2 * i + 1])

    def set(self, i, x):  # O(log(n))
        i += self.size
        self.tree[i] = x
        while i:
            i >>= 1
            self.tree[i] = self.fx(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, i, x):
        i += self.size
        self.tree[i] = x
        while i > 1:
            i >>= 1
            self.tree[i] = self.fx(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):  # l = r の場合はたぶんバグるので注意
        tmp_l = self.ex
        tmp_r = self.ex
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                tmp_l = self.fx(tmp_l, self.tree[l])
                l += 1
            if r & 1:
                tmp_r = self.fx(self.tree[r - 1], tmp_r)  # 交換法則を仮定しない(順序大事に)
            l >>= 1
            r >>= 1
        return self.fx(tmp_l, tmp_r)

    def get(self, i):
        return self.tree[self.size + i]

    def show(self):
        return self.tree[self.size: self.size + self.n]

# ---------------------- #

n = int(input())
LR = [tuple(int(x) for x in input().split()) for _ in range(n)]
LR.sort(key=itemgetter(0))
L = []
R = []
for l, r in LR:
    L.append(l)
    R.append(r)
seg = SegTree(R, fx=min, ex=10**18)
ans = 0
for i in range(1, n):
    contest1 = seg.query(0, i) - L[i - 1] + 1
    contest2 = seg.query(i, n) - L[n - 1] + 1
    ans = max(ans, contest1 + contest2)

LR.sort(key=lambda item: item[1] - item[0], reverse=True)
lmax = max(l for l, _ in LR[1:])
rmin = min(r for _, r in LR[1:])
ans = max(ans, LR[0][1] - LR[0][0] + 1 + max(rmin - lmax + 1, 0))
print(ans)
