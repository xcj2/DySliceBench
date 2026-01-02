# http://tsutaj.hatenablog.com/entry/2017/03/29/204841
class SegmentTree:
    def __init__(self, v, func, init_val):
        self.func = func
        self.init_val = init_val

        sz = len(v)

        self.n = 1
        while self.n < sz:
            self.n *= 2

        self.node = [self.init_val for _ in range(2 * self.n - 1)]
        # 元配列 v をセグメント木で表現する
        # 最下段のノード数は元配列のサイズ以上になる最小の 2 冪 -> これを n とおく
        # セグメント木全体で必要なノード数は 2n - 1 個である

        for i in range(sz):
            self.node[i + self.n - 1] = v[i]
        # 最下段に値を入れたあとに、下の段から順番に値を入れる

        for i in range(self.n - 2, -1, -1):
            self.node[i] = self.func(self.node[2 * i + 1], self.node[2 * i + 2])
        # 値を入れるには、自分の子の 2 値を参照すれば良い

    def update(self, x, val):
        x += self.n - 1
        # 最下段のノードにアクセスする

        self.node[x] = val
        while x > 0:
            x = (x - 1) // 2
            self.node[x] = self.func(self.node[2 * x + 1], self.node[2 * x + 2])
        # 最下段のノードを更新したら、あとは親に上って更新していく

    # 要求区間 [a, b) 中の要素の最小値を答える
    # k := 自分がいるノードのインデックス
    # 対象区間は [l, r) にあたる

    def get_val(self, a, b, k, l, r):
        if r <= a or b <= l: return self.init_val
        # 要求区間と対象区間が交わらない -> 適当に返す

        if a <= l and r <= b: return self.node[k]
        # 要求区間が対象区間を完全に被覆 -> 対象区間を答えの計算に使う

        vl = self.get_val(a, b, 2 * k + 1, l, (l + r) // 2)
        vr = self.get_val(a, b, 2 * k + 2, (l + r) // 2, r)
        return self.func(vl, vr)
        # 要求区間が対象区間の一部を被覆 -> 子について探索を行う
        # 左側の子を vl ・ 右側の子を vr としている
        # 新しい対象区間は、現在の対象区間を半分に割ったもの


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


N = int(input())
a = tuple(map(int, input().split()))

st = SegmentTree(v=a, func=gcd, init_val=0)

g = max(
    gcd(
        st.get_val(0, drop_idx, 0, 0, st.n),
        st.get_val(drop_idx + 1, N, 0, 0, st.n)
    ) for drop_idx in range(N)
)
print(g)
