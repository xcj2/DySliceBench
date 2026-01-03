class UnionFind():
    """
    UnionFindTreeのクラス
    
    Attributes:
    n: int: ノード数
    parents: そのノードが属する木の根を格納, 根の場合は-1

    """
    def __init__(self, n):
        """ノード数nで初期化"""
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """ノードxが属するグループの根を返す"""
        if self.parents[x] < 0:
            return x
        else:
            #経路圧縮
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """xが属するグループとyが属するグループを併合"""
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """xが属するグループの要素数を返す"""
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """x, yが同じグループに属するかどうかを返す"""
        return self.find(x) == self.find(y)

    def members(self, x):
        """xが属するグループ内の要素をリストで返す"""
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """全ての根に対する要素をリストで返す"""
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """グループの総数を返す"""
        return len(self.roots())

    def all_group_members(self):
        """{root: [そのグループの要素リスト]}の辞書を返す"""
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        """printデバッグ用. root: [要素リスト]をstrで返す"""
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def kruskal(edge_list: list, n_V: int):
    """
    クラスカル法
    edge_list: 各要素が(weight, node1, node2)のリスト
    n_V: ノード数
    sortがボトルネックとなりO(|E|log(|E|))
    """
    edge_list = sorted(edge_list) # 重み昇順に整列
    ret = 0
    uf = UnionFind(n_V) # UnionFind
    n_edges = 0
    for w, s, t in edge_list:
        if n_edges == n_V-1: #全域木になったら終了
            break
        if uf.same(s, t):
            #s, tが同じグループの場合,
            #構築するものが木ではなくなってしまう(閉路ができる)
            #のでcontinue
            continue
        
        uf.union(s, t) # s, tを併合
        ret += w
        n_edges += 1
    
    return ret

N = int(input())
x = []
y = []
for i in range(N):
    a, b = map(int, input().split())
    x.append((a, i))
    y.append((b, i))

edges = []
x.sort()
y.sort()
for i in range(N-1):
    id1 = x[i][1]
    id2 = x[i+1][1]
    cost = abs(x[i][0]-x[i+1][0])
    edges.append((cost, id1, id2))
for i in range(N-1):
    id1 = y[i][1]
    id2 = y[i+1][1]
    cost = abs(y[i][0]-y[i+1][0])
    edges.append((cost, id1, id2))

ret = kruskal(edges, N)
print(ret)