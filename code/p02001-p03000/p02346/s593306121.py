class SegmentTree:
    '''
    SegmentTree(arr, e)
        arr : 配列,
        e : 単位元\n
    segment_tree[i] = x で更新\n
    segment_tree[a,b] で区間[a,b)の計算結果を得る(a<bでなければ単位元が返ってくる)
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



# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_B
n, q = map(int, input().split())
A = [0] * n
st = SegmentTree(A, 0)
for i in range(q):
    com, x, y = map(int, input().split())
    x -= 1
    if com == 0:
        st[x] += y
    else:
        y -= 1
        # print(st[x: y + 1])
        print(st.query(x, y + 1))

