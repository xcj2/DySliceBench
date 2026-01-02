import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(N)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
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
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, left, right):
        """
        [left, right)のsegfuncしたものを得る
        left: index(0-index)
        right: index(0-index)
        """
        res = self.ide_ele
        left += self.num
        right += self.num
        while left < right:
            if left & 1:
                res = self.segfunc(res, self.tree[left])
                left += 1
            if right & 1:
                res = self.segfunc(res, self.tree[right - 1])
            left >>= 1
            right >>= 1
        return res


def resolve():
    n, k = map(int, input().split())
    P = list(map(int, input().split()))

    seg_min = SegTree(P, lambda x, y: min(x, y), f_inf)
    seg_max = SegTree(P, lambda x, y: max(x, y), -f_inf)
    mi = seg_min.query(0, k)
    ma = seg_max.query(0, k)
    res = {(0, k - 1)}
    for i in range(1, n - k + 1):
        prev = P[i - 1]
        new = P[i + k - 1]
        if prev != mi or new < ma:
            res.add((i, i + k - 1))
        mi = seg_min.query(i, i + k)
        ma = seg_max.query(i, i + k)

    ascending = []
    head = 0
    foot = 1
    cnt = 1
    for i in range(1, n):
        if P[i - 1] < P[i]:
            cnt += 1
            foot = i
        else:
            cnt = 1
            head = i
        if cnt == k:
            ascending.append((head, foot))
            head = i
            cnt -= 1

    ans = len(res)
    flg = False
    for section in ascending:
        if section in res:
            if not flg:
                flg = True
            else:
                ans -= 1
    print(ans)


if __name__ == '__main__':
    resolve()
