class SegTree(object):
    # 区間の中で v 以下の値のうち最も左にある値と index を取得
    # 普通のセグ木に get_threshold_left と get_threshold_left_all を加えただけ
    # 検証1: https://atcoder.jp/contests/arc038/submissions/6933949 (全区間のみ)
    # 検証2: https://atcoder.jp/contests/arc046/submissions/7430924 (全区間のみ)
    # 抽象化したい
    __slots__ = ["elem_size", "tree", "default", "op"]
    def __init__(self, a: list, default=float("inf"), op=min):
        from math import ceil, log
        real_size = len(a)
        self.elem_size = elem_size = 1 << ceil(log(real_size, 2))
        self.tree = tree = [default] * (elem_size * 2)
        tree[elem_size:elem_size + real_size] = a
        self.default = default
        self.op = op
        for i in range(elem_size - 1, 0, -1):
            tree[i] = op(tree[i << 1], tree[(i << 1) + 1])

    def get_value(self, x: int, y: int) -> int:  # 半開区間
        l, r = x + self.elem_size, y + self.elem_size
        tree, result, op = self.tree, self.default, self.op
        while l < r:
            if l & 1:
                result = op(tree[l], result)
                l += 1
            if r & 1:
                r -= 1
                result = op(tree[r], result)
            l, r = l >> 1, r >> 1
        return result

    def get_threshold_left(self, x, y, v):
        # 区間 [x, y) 内で一番左の v 以下の値
        tree, result, op, elem_size = self.tree, self.default, self.op, self.elem_size
        l, r = x + elem_size, y + elem_size
        idx_left = idx_right = -1  # 内部 index
        while l < r:
            if l & 1:
                result = op(tree[l], result)
                if idx_left == -1 and tree[l] <= v:
                    idx_left = l
                l += 1
            if r & 1:
                r -= 1
                result = op(tree[r], result)
                if tree[r] <= v:
                    idx_right = r
            l, r = l >> 1, r >> 1
        if idx_left==idx_right==-1:
            return -1, -1
        idx = idx_left if idx_left!=-1 else idx_right
        while idx < elem_size:
            idx <<= 1
            if tree[idx] > v:
                idx += 1
        return tree[idx], idx-elem_size

    def get_threshold_left_all(self, v):
        # 全区間で一番左の v 以下の値
        tree, op, elem_size = self.tree, self.op, self.elem_size
        if tree[1] > v:
            return -1, -1
        idx = 1
        while idx < elem_size:
            idx <<= 1
            if tree[idx] > v:
                idx += 1
        return tree[idx], idx-elem_size

    def set_value(self, i: int, value: int) -> None:
        k = self.elem_size + i
        self.tree[k] = value
        self.update(k)

    def update(self, i: int) -> None:
        op, tree = self.op, self.tree
        while i > 1:
            i >>= 1
            tree[i] = op(tree[i << 1], tree[(i << 1) + 1])



N, M = map(int, input().split())
S = list(map(int, input()))
dp = [10**9] * (N+1)
seg = SegTree(dp)
from_ = [-10000000] * (N+1)
seg.set_value(0, 0)
for i, c in enumerate(S[1:], 1):
    if c==1:
        continue
    v, idx = seg.get_threshold_left(max(i-M, 0), i, 1000000)
    if v==-1:
        print(-1)
        exit()
    from_[i] = idx
    seg.set_value(i, v+1)
n = seg.tree[N + seg.elem_size]
#print(seg.tree[seg.elem_size:seg.elem_size+N+1])
#print(from_)

Ans = []
v = N
while v != 0:
    v_ = from_[v]
    Ans.append(v-v_)
    v = v_
Ans.reverse()
print(" ".join(map(str, Ans)))
