#####################################################################################################
##### Lazy Propotional Segment tree (遅延区間比例セグメント木)
#####################################################################################################

"""
区間更新、区間取得が可能

セグ木の深さ毎でモノイド間の作用 g の振る舞いが異なってしまう場合がある。
実際のところ、作用 g は大域的作用である必要はなく、時間効率そのままで局所変数を一つ持たせて局所化することができる。
ただし、一般化された分配法則
g[i](x*y) = g[i<<1]x * g[(i<<1)|1]x
を満たす必要がある。

以下の例では、 セグ木の i 番目のノードを構成する要素の数（何個の要素の積か？）を l[i] として、
g[i]x = x*l[i]
という局所作用を考えている。

例)

RSQ and RUQ:
http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=4777823#2

# クエリ関数
ef = 0
f = lambda x, y : x+y
# 更新関数
eh = -(1<<24)
h = lambda x, y: x if x != eh else y
g = lambda x, y, l: x*l

#################################################################################
#################################################################################


解説
https://maspypy.com/segment-tree-%E3%81%AE%E3%81%8A%E5%8B%89%E5%BC%B72
https://smijake3.hatenablog.com/entry/2018/11/03/100133

解説（作用付きモノイド）
https://algo-logic.info/segment-tree/

参考コード（C++）
https://ei1333.github.io/library/library/structure/segment-tree/lazy-segment-tree.cpp.html

参考コード(python)
https://yukicoder.me/submissions/470340


"""


class LazyPropSegmentTree():

    def __init__(self, n, f, g, h, ef, eh):
        """
        :param n: 配列の要素数
        :param f: 取得半群の元同士の積を定義
        :param g: 更新半群の元 xh が配列上の実際の値にどのように作用するかを定義
        :param h: 更新半群の元同士の積を定義　（更新半群の元を xh と表記）
        :param x: 配列の各要素の値。treeの葉以外は xf(x1,x2,...)
        :param length: 添え字 i がいくつの要素を畳み込んだ値になっているか
        """
        self.n = n
        self.f = f
        self.g = lambda xh, x, l: g(xh, x, l) if xh != eh else x
        self.h = h
        self.ef = ef
        self.eh = eh
        l = (self.n - 1).bit_length()
        self.size = 1 << l
        self.tree = [self.ef] * (self.size << 1)
        self.lazy = [self.eh] * ((self.size << 1) + 1)
        self.plt_cnt = 0
        self.length = [0]
        for i in range(l+1):
            self.length += [1<<(l-i)]*(1<<i)

    def built(self, array):
        """
        arrayを初期値とするセグメント木を構築
        """
        size, tree, f = self.size, self.tree, self.f
        for i in range(self.n):
            tree[size + i] = array[i]
        for i in range(size - 1, 0, -1):
            tree[i] = f(tree[i<<1], tree[(i<<1)|1])

    def update(self, i, x):
        """
        i 番目の要素を x に更新する
        """
        size, tree, lazy, eh = self.size, self.tree, self.lazy, self.eh
        i += size
        self.propagate_lazy(i)
        tree[i] = x
        lazy[i] = eh
        self.propagate_tree(i)

    def get(self, i):
        """
        i 番目の値を取得（ 0-indexed ） ( O(logN) )
        """
        size, tree, lazy, length, g = self.size, self.tree, self.lazy, self.length, self.g
        i += size
        self.propagate_lazy(i)
        return g(lazy[i], tree[i], length[i])

    def update_range(self, l, r, x):
        """
        半開区間 [l, r) の各々の要素 a に op(x, a)を作用させる （ 0-indexed ）　（ O(logN) ）
        """
        size, lazy, h = self.size, self.lazy, self.h
        if l >= r:
            return
        l += size
        r += size
        l0 = l//(l&-l)
        r0 = r//(r&-r)
        self.propagate_lazy(l0)
        self.propagate_lazy(r0-1)
        while l < r:
            if r&1:
                r -= 1              # 半開区間なので先に引いてる
                lazy[r] = h(x, lazy[r])
            if l&1:
                lazy[l] = h(x, lazy[l])
                l += 1
            l >>= 1
            r >>= 1
        self.propagate_tree(l0)
        self.propagate_tree(r0-1)

    def get_range(self, l, r):
        """
        [l, r)の区間取得の結果を返す　(0-indexed)
        """
        size, tree, lazy, length, ef, f, g = self.size, self.tree, self.lazy, self.length, self.ef, self.f, self.g
        l += size
        r += size
        self.propagate_lazy(l//(l&-l))
        self.propagate_lazy((r//(r&-r))-1)
        res_l = ef
        res_r = ef
        while l < r:
            if l & 1:
                res_l = f(res_l, g(lazy[l], tree[l], length[l]))
                l += 1
            if r & 1:
                r -= 1
                res_r = f(g(lazy[r], tree[r], length[r]), res_r)
            l >>= 1
            r >>= 1
        return f(res_l, res_r)

    def max_right(self, l, z):
        """
        以下の条件を両方満たす r を(いずれか一つ)返す
            ・r = l or f(op(a[l], a[l + 1], ..., a[r - 1])) = true
            ・r = n or f(op(a[l], a[l + 1], ..., a[r])) = false
        """
        if l >= self.n: return self.n
        l += self.size
        s = self.ef
        while 1:
            while l % 2 == 0:
                l >>= 1
            if not z(self.f(s, self.g(self.lazy[l], self.tree[l], self.length[l]))):
                while l < self.size:
                    l *= 2
                    if z(self.f(s, self.g(self.lazy[l], self.tree[l], self.length[l]))):
                        s = self.f(s, self.g(self.lazy[l], self.tree[l], self.length[l]))
                        l += 1
                return l - self.size
            s = self.f(s, self.g(self.lazy[l], self.tree[l], self.length[l]))
            l += 1
            if l & -l == l: break
        return self.n

    def min_left(self, r, z):
        """
        以下の条件を両方満たす l を(いずれか一つ)返す
            ・l = r or f(op(a[l], a[l + 1], ..., a[r - 1])) = true
            ・l = 0 or f(op(a[l - 1], a[l], ..., a[r - 1])) = false
        """
        if r <= 0: return 0
        r += self.size
        s = self.ef
        while 1:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not z(self.f(self.g(self.lazy[r], self.tree[r]), s)):
                while r < self.size:
                    r = r * 2 + 1
                    if z(self.f(self.g(self.lazy[r], self.tree[r]), s)):
                        s = self.f(self.g(self.lazy[r], self.tree[r]), s)
                        r -= 1
                return r + 1 - self.size
            s = self.f(self.g(self.lazy[r], self.tree[r]), s)
            if r & -r == r: break
        return 0

    def propagate_lazy(self, i):
        """
        lazy の値をトップダウンで更新する　（ O(logN) ）
        """
        tree, lazy, length, eh, h, f, g = self.tree, self.lazy, self.length, self.eh, self.h, self.f, self.g
        for k in range(i.bit_length()-1,0,-1):
            x = i>>k
            if lazy[x] == eh:
                continue
            laz = lazy[x]
            lazy[(x<<1)|1] = h(laz, lazy[(x<<1)|1])
            lazy[x<<1] = h(laz, lazy[x<<1])
            tree[x] = g(laz, tree[x], length[x])   # get_range ではボトムアップの伝搬を行わないため、この処理をしないと tree が更新されない
            lazy[x] = eh

    def propagate_tree(self, i):
        """
        tree の値をボトムアップで更新する　（ O(logN) ）
        """
        tree, lazy, length, f, g = self.tree, self.lazy, self.length, self.f, self.g
        while i>1:
            i>>=1
            tree[i] = f(g(lazy[i<<1], tree[i<<1], length[i<<1]), g(lazy[(i<<1)|1], tree[(i<<1)|1], length[i<<1]))

    def __getitem__(self, i):
        return self.get(i)

    def __iter__(self):
        size, tree, lazy, length, eh, h, g = self.size, self.tree, self.lazy, self.length, self.eh, self.h, self.g
        for x in range(1, size):
            if lazy[x] == eh:
                continue
            lazy[(x<<1)|1] = h(lazy[x], lazy[(x<<1)|1])
            lazy[x<<1] = h(lazy[x], lazy[x<<1])
            self.tree[x] = self.g(self.lazy[x], self.tree[x])
            lazy[x] = eh
        for xh, x in zip(lazy[size:size+self.n], tree[size:size+self.n]):
            yield g(xh,x,1)

    def __str__(self):
        return str(list(self))

    def debug(self):
        tree, lazy = self.tree, self.lazy
        def full_tree_pos(G):
            n = G.number_of_nodes()
            if n == 0: return {}
            pos = {0: (0.5, 0.9)}
            if n == 1: return pos
            i = 1
            while not n >= 2 ** i or not n < 2 ** (i + 1): i+=1
            height = i
            p_key, p_y, p_x = 0, 0.9, 0.5
            l_child = True
            for i in range(height):
                for j in range(2 ** (i + 1)):
                    if 2 ** (i + 1) + j - 1 < n:
                        if l_child == True:
                            pos[2 ** (i + 1) + j - 1] = (p_x - 0.2 / (i * i + 1), p_y - 0.1)
                            G.add_edge(2 ** (i + 1) + j - 1, p_key)
                            l_child = False
                        else:
                            pos[2 ** (i + 1) + j - 1] = (p_x + 0.2 / (i * i + 1), p_y - 0.1)
                            l_child = True
                            G.add_edge(2 ** (i + 1) + j - 1, p_key)
                            p_key += 1
                            (p_x, p_y) = pos[p_key]
            return pos

        import networkx as nx
        import matplotlib.pyplot as plt
        A = tree[1:]
        G = nx.Graph()
        labels = {}
        for i, a in enumerate(A):
            G.add_node(i)
            labels[i] = a
        pos = full_tree_pos(G)
        nx.draw(G, pos=pos, with_labels=True, labels=labels, node_size=1000)
        plt.savefig("tree-{0}.png".format(self.plt_cnt))
        plt.clf()

        A = lazy[1:-1]
        G = nx.Graph()
        labels = {}
        for i, a in enumerate(A):
            G.add_node(i)
            labels[i] = a
        pos = full_tree_pos(G)
        nx.draw(G, pos=pos, with_labels=True, labels=labels, node_size=1000)
        plt.savefig("lazy-{0}.png".format(self.plt_cnt))
        plt.clf()
        self.plt_cnt += 1

##################################################################################################################
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
ef = 0
eh = 0
f = lambda x, y: x if x > y else y
g = lambda x, y, s: x if x > y else y
h = lambda x, y: x if x > y else y
st = LazyPropSegmentTree(N, f, g, h, ef, eh)
st.built(A)
res = []

for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        st.update(x - 1, y)
    elif t == 2:
        res.append(st.get_range(x - 1, y))
    else:
        res.append(st.max_right(x - 1, lambda z: z < y) + 1)

print('\n'.join(map(str, res)))