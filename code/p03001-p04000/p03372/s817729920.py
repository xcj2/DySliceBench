from itertools import accumulate

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

n, c = (int(x) for x in input().split())
X = []
V = []
D = []
prev_x = 0
for _ in range(n):
    x, v = (int(x) for x in input().split())
    X.append(x)
    D.append(x - prev_x)
    V.append(v)
    prev_x = x
D.append(c - X[-1])
rev_D = list(reversed(D))
rev_V = list(reversed(V))

ans = 0
# 時計回り
A = [0] * n
for i in range(n):
    A[i] = V[i] - D[i]
acc_A = list(accumulate(A))
ans = max(ans, max(acc_A))

# 反時計回り
B = [0] * n
for i in range(n):
    B[i] = rev_V[i] - rev_D[i]
acc_B = list(accumulate(B))
ans = max(ans, max(acc_B))

# 時計回りからの反時計回り i個まで食べて向きを変える
seg_B = SegTree(acc_B, fx=max, ex=-10**18)
tmp = 0
for i in range(n - 1):
    tmp_cal = acc_A[i] - X[i]  # 食べて原点まで戻った時点のカロリー
    tmp = max(tmp, tmp_cal + seg_B.query(0, n-i-1))
ans = max(ans, tmp)

# 反時計回りからの時計回り
seg_A = SegTree(acc_A, fx=max, ex=-10**18)
tmp = 0
for i in range(n - 1):
    tmp_cal = acc_B[i] - (c - X[-i - 1])  # 食べて原点まで戻った時点のカロリー
    tmp = max(tmp, tmp_cal + seg_A.query(0, n-i-1))
ans = max(ans, tmp)

print(ans)
