# Monoidクラスに+*/を定義するとLazySegmentTreeを使う時に便利？


# 1-indexed
class SegmentTree:
    '''
    SegmentTree(arr, e)
        arr : 配列,
        e : 単位元\n
    segment_tree[i] で取得、更新\n
    segment_tree.query(a,b) で区間[a,b)の計算結果を得る(a<bでなければ単位元が返ってくる)
    '''
    def __init__(self, arr, e):
        self.e = e
        self.len = len(arr)
        # 最下層の長さnの初期化(扱う配列の長さ以上の2冪のうち最も小さいもの)
        n = 2 ** (len(bin(self.len + 1)) - 2)
        self.n = n
        # nodeの初期化
        node = [e] * (2 * n)
        node[n: n + self.len] = arr
        for i in range(n - 1, 0, -1):
            node[i] = node[2 * i] + node[2 * i + 1]
        self.node = node

    def __setitem__(self, i, val):
        # 最下層からはじめる。それより上にはn-1個のノードがある
        i += self.n
        self.node[i] = val
        # 最上層に辿り着くまで
        while i > 1:
            # 親に移動
            i //= 2
            # 2つの子に対する計算結果
            self.node[i] = self.node[2 * i] + self.node[2 * i + 1]

    def __getitem__(self, i):
        return self.node[self.n + i]

    def query(self, a, b):
        a = self.trim(a, self.len)
        b = self.trim(b, self.len)

        # [a,b)が欲しい
        # k=0, [l=0,r=n)から始める
        # [l,r)が[a,b)の中に入るまで[l,mid), [mid,r)に分割して再帰
        def get(k, l, r):
            # そもそも[l,r)が[a,b)に入ってない時は計算に影響を与えない単位元を返す
            if r <= a or b <= l:
                return self.e
            if a <= l and r <= b:
                return self.node[k]
            m = (l + r) // 2
            return get(2 * k, l, m) + get(2 * k + 1, m, r)

        return get(1, 0, self.n)

    def getlist(self):
        return self.node[self.n:]

    def trim(self, i, n):
        i = max(i, -n)
        i = min(i, n)
        if i < 0:
            i += n
        return i

# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_A

# 一例　([0..2^31-1],min)のモノイド
class Monoid:
    '''
    Monoid(val)\n
    演算は自分で定義する Monoid + Monoid
    ※単位元をクラス変数とし持たない
    '''

    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return repr(self.val)

    # 以下自分で定義
    def __add__(self, other):
        return Monoid(min(self.val, other.val))

n, q = map(int, input().split())
A = [Monoid(2 ** 31 - 1)] * n
st = SegmentTree(A, Monoid(2 ** 31 - 1))
for i in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        st[x] = Monoid(y)
    else:
        print(st.query(x, y + 1))

