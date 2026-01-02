class SegTreeIndex(object):
    # 区間の最小 or 最大値とその index を取得
    # 検証: https://yukicoder.me/submissions/376308
    __slots__ = ["elem_size", "tree", "default", "op", "index", "op2"]
    def __init__(self, a: list, default=float("inf"), op=lambda a,b: b if a>b else a, op2=lambda a,b:a>b):
        # 同じ場合最左のインデックスを返す
        # 最大値・最左 -> -float("inf"), max, lambda a,b:a<=b
        from math import ceil, log
        real_size = len(a)
        self.elem_size = elem_size = 1 << ceil(log(real_size, 2))
        self.tree = tree = [default] * (elem_size * 2)
        self.index = index = [0] * (elem_size * 2)
        tree[elem_size:elem_size + real_size] = a
        index[elem_size:elem_size + real_size] = list(range(real_size))
        self.default = default
        self.op = op
        self.op2 = op2
        for i in range(elem_size-1, 0, -1):
            v1, v2 = tree[i<<1], tree[(i<<1)+1]
            tree[i] = op(v1, v2)
            index[i] = index[(i<<1) + op2(v1, v2)]

    def get_value(self, x: int, y: int) -> tuple:  # 半開区間
        l, r = x + self.elem_size, y + self.elem_size
        tree, op, op2, index = self.tree, self.op, self.op2, self.index
        result_l = result_r = self.default
        idx_l = idx_r = -1
        while l < r:
            if l & 1:
                v1, v2 = result_l, tree[l]
                result_l = op(v1, v2)
                if op2(v1, v2)==1:
                    idx_l = index[l]
                l += 1
            if r & 1:
                r -= 1
                v1, v2 = tree[r], result_r
                result_r = op(v1, v2)
                if op2(v1, v2)==0:
                    idx_r = index[r]
            l, r = l >> 1, r >> 1
        result = op(result_l, result_r)
        idx = idx_r if op2(result_l, result_r) else idx_l
        return result, idx

    def set_value(self, i: int, value: int) -> None:
        k = self.elem_size + i
        self.tree[k] = value
        self.update(k)

    def update(self, i: int) -> None:
        op, tree, index, op2 = self.op, self.tree, self.index, self.op2
        while i > 1:
            i >>= 1
            v1, v2 = tree[i<<1], tree[(i<<1)+1]
            tree[i] = op(v1, v2)
            index[i] = index[(i<<1) + op2(v1, v2)]


N, M = map(int, input().split())
S = list(map(int, input()))
dp = [10 ** 9] * (N + 1)
seg = SegTreeIndex(dp)
from_ = [-10000000] * (N + 1)
seg.set_value(0, 0)
for i, c in enumerate(S[1:], 1):
    if c == 1:
        continue
    v, idx = seg.get_value(max(i - M, 0), i)
    if v == 1000000000:
        print(-1)
        exit()
    from_[i] = idx
    seg.set_value(i, v + 1)
n = seg.tree[N + seg.elem_size]
# print(seg.tree[seg.elem_size:seg.elem_size+N+1])
# print(from_)

Ans = []
v = N
while v != 0:
    v_ = from_[v]
    Ans.append(v - v_)
    v = v_
Ans.reverse()
print(" ".join(map(str, Ans)))
