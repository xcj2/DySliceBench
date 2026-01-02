def e_simple_string_queries():
    # 参考: https://atcoder.jp/contests/abc157/submissions/10481866
    N = int(input())
    S = input()
    Q = int(input())
    Queries = [input().split() for _ in range(Q)]

    class SegmentTree(object):
        """
        Segment Tree (0-indexed)
        1. update:  k 番目の値を x に更新する
        2. query: 区間 [l, r) の値を得る
        """

        def __init__(self, n, func, identity, init_list=[]):
            """
            n: 要素数
            func: 値の操作に使う関数 (min, max, add, gcd, etc.)
            identity: func に対する単位元
            init_list: 設定されていれば、それで初期化する
            """
            self.n = n
            self.func = func
            self.identity = identity

            # n を超える最小の 2 の冪乗
            self.pow2 = 1
            while self.pow2 < n:
                self.pow2 <<= 1

            self.tree = [self.identity] * (self.pow2 << 1)

            # 初期化を指定していた場合
            if init_list:
                # 木の最下段の初期化
                for k in range(n):
                    self.tree[k + self.pow2] = init_list[k]
                # 木の根へ初期化
                for k in range(self.pow2 - 1, -1, -1):
                    self.tree[k] = self.func(self.tree[k * 2], self.tree[k * 2 + 1])

        def update(self, k, x):
            """k 番目の値を x に更新"""
            pos = k + self.pow2
            self.tree[pos] = x  # 木の葉 (元の配列に当たる) を変更
            # 木の根に向かって更新を反映
            while pos > 0:
                pos >>= 1
                self.tree[pos] = self.func(self.tree[pos * 2], self.tree[pos * 2 + 1])

        def query(self, a, b):
            """区間 [a, b) について self.func を通した値を得る"""
            left = a + self.pow2
            right = b + self.pow2
            ret = self.identity
            while left < right:
                if right & 1:
                    right -= 1
                    ret = self.func(ret, self.tree[right])
                if left & 1:
                    ret = self.func(ret, self.tree[left])
                    left += 1
                left >>= 1
                right >>= 1
            return ret

        def get(self, k):
            """k 番目の値を取得"""
            return self.tree[k + self.pow2]

        def get_all(self):
            """[0, n) の値を取得"""
            return self.tree[1]

        def __str__(self):
            return ' '.join(map(str, [self.get(k) for k in range(self.n)]))

    def popcount(n):
        """n を 2 進表記したとき、1 となっているビットの数"""
        return bin(n).count('1')

    s = [ord(ch) - 97 for ch in S]  # ord('a') => 97
    # 文字を Unicode コードポイントで持つことで、
    # セグメント木で「[l, r) に現れる文字」を管理できる
    segtree = SegmentTree(N, lambda a, b: a | b, 0, [1 << ch for ch in s])

    ans = []
    for q, s1, s2 in Queries:
        if q == '1':
            i, ch = int(s1) - 1, ord(s2) - 97
            # s[i] == ch のときに下の処理を行うと正しく動作しない
            # (ch == prev のとき xor をとると 0 になってしまう)
            if s[i] != ch:
                prev = s[i]
                s[i] = ch
                # これまでの文字列に新しい文字を追加し (bitwise-or)、
                # 古い文字を消す (bitwise-xor)
                segtree.update(i, (segtree.get(i) | 1 << ch) ^ (1 << prev))
        elif q == '2':
            left, right = int(s1) - 1, int(s2) - 1
            # 立っているビットの数が文字種数となるように管理している
            ans.append(popcount(segtree.query(left, right + 1)))
    return '\n'.join(map(str, ans))

print(e_simple_string_queries())