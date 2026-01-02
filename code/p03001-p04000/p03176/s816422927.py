class SegmentTree:
    def __init__(self, a: list, e: 'default', f: 'function'):
        n = len(a)
        size = 1 << (n - 1).bit_length()  # 元の配列サイズ以上の最小の二冪 == 最下段
        v = [e] * (size * 2 - 1)
        for i in range(n):
            # size-1個の上段の次、size個目からn個が元の配列の代入位置
            v[size - 1 + i] = a[i]
        for i in range(size - 2, -1, -1):
            v[i] = f(v[i * 2 + 1], v[i * 2 + 2])

        self.n = n  # 元の配列の長さ
        self.size = size  # 元の配列サイズ以上の最小の二冪 == 最下段の要素数
        self.v = v  # Segtreeの配列
        self.e = e  # 初期値
        self.f = f  # 比較関数

    def update(self, k: 'index', x: 'val'):
        k += self.size - 1  # 最下段のindexに変更する
        self.v[k] = x  # 値を更新する
        while k > 0:
            k = (k - 1) // 2  # 親のindex
            self.v[k] = self.f(self.v[k * 2 + 1], self.v[k * 2 + 2])

    def get(self, a, b, k=0, l=0, r=-1):
        # [a,b)区間の処理結果を返す
        # 注目区間[l,r)
        if r < 0:
            r = self.size

        if r <= a or b <= l:
            return self.e
        # 区間が重ならない

        if a <= l and r <= b:
            return self.v[k]
        # 完全被覆

        m = (l + r) // 2
        return self.f(self.get(a, b, k * 2 + 1, l, m), self.get(a, b, k * 2 + 2, m, r))
        # 部分被覆


def solve(n, h, a):
    seg = SegmentTree([0] * (n + 1), 0, max)
    for i in range(n):
        seg.update(h[i], seg.get(0, h[i]) + a[i])
        # 1回あたり更新するのは1箇所だから、iを状態にもつ必要はなくて、配列を使い回すことができる
        # 区間maxが高速に計算できればいいから、セグメント木を使えばできる
    return seg.get(0, n + 1)


if __name__ == '__main__':
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = tuple(map(int, input().split()))
    a = tuple(map(int, input().split()))
    print(solve(n, h, a))

# https://kyopro-friends.hatenablog.com/entry/2019/01/12/231035
# classやめた方が遅かった
# 比較関数minがグローバルにあるから、遅くなっていた？

