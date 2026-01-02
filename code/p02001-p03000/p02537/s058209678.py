import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


class SegTree:
    """
    Segment Tree
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        初期化

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
            self.tree[i] = segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新 O(N)

        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る O(logN)

        l: index(0-index)
        r: index(0-index)
        """
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


def main():
    N, K = map(int, input().split())
    A = []
    MAX = 300005
    for i in range(N):
        A.append(int(input()))

    ide_ele = 0

    dp = SegTree([0] * MAX, segfunc=max, ide_ele=ide_ele)

    for i in range(N):
        a = A[i]
        l = max(0, a - K)
        r = min(MAX, a + K + 1)
        now = dp.query(l, r) + 1
        dp.update(a, now)

    print(dp.query(0, MAX))


if __name__ == "__main__":
    main()
