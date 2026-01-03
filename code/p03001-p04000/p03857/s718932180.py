class UnionFind :
    """
    Union Find木
    ---
    頂点のインデックスは0~

    Attributes
    ---
    parent : list<int>
        親のリスト．parent[頂点のインデックス] = 親のインデックス
    height : list<int>
        各木の高さ
    size : list<int>
        各木の頂点数
    component : int
        連結成分の数
    """

    def __init__(self, size) :
        """
        Parameters
        ---
        size : int
            頂点数
        """
        self.parent = list(range(size))
        self.height = [0] * size
        self.size = [1] * size
        self.component = size

    def root(self, index) :
        """
        親のインデックスの取得

        Parameters
        ---
        index : int
            取得する頂点のインデックス

        Returns
        ---
        rootIndex : int
            指定した頂点の根のインデックス
        """
        if self.parent[index] == index :  # 根の場合
            return index
        rootIndex = self.root(self.parent[index])  # 葉の場合親の根を取得
        self.parent[index] = rootIndex  # 親の付け直し
        return rootIndex

    def union(self, index1, index2) :  # 結合
        """
        木の結合

        Parameters
        ---
        index1 : int
        index2 : int
            結合する頂点のインデックス
        """
        root1 = self.root(index1)
        root2 = self.root(index2)

        if root1 == root2 :  # 連結されている場合
            return

        root1, root2 = min(root1, root2), max(root1, root2)
        self.parent[root2] = root1


    def isSameRoot(self, index1, index2) :
        """
        同じ木に属するかを判定する

        Parameters
        ---
        index1 : int
        index2 : int

        Returns
        ---
        boolean
        """
        return self.root(index1) == self.root(index2)

    def sizeOfSameRoot(self, index) :
        """
        指定した頂点の属する木の大きさを取得する
        """
        return self.size[self.root(index)]

    def getComponent(self) :
        """
        連結成分数を取得する
        """
        return self.component

from collections import Counter
N, K, L = map(int, input().split())

train = UnionFind(N)
road = UnionFind(N)

for _ in range(K):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    train.union(p, q)

for _ in range(L):
    r, s = map(int, input().split())
    r -= 1
    s -= 1
    road.union(r, s)

countList = []
for i in range(N):
    countList.append((train.root(i), road.root(i)))

count = Counter(countList)
ans = [count[(train.root(i), road.root(i))] for i in range(N)]
print(*ans)