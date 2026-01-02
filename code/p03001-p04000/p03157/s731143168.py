from collections import deque
from collections import defaultdict

H, W = map(int, input().split())
chart = [input() for _ in range(H)]

class UnionFind :
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

        self.component -= 1  # 連結成分を減らす

        if self.height[root1] < self.height[root2] :
            self.parent[root1] = root2  # root2に結合
            self.size[root2] += self.size[root1]
        else :
            self.parent[root2] = root1  # root1に結合
            self.size[root1] += self.size[root2]
            if self.height[root1] == self.height[root2] :
                self.height[root1] += 1
        return

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

tree = UnionFind(H * W)
visited = [[False] * W for _ in range(H)]

def f(h, w):
    return h * W + w

def search(h, w):
    que = deque([(h, w)])

    while que:
        nh, nw = que.popleft()
        if visited[nh][nw]:
            continue
        visited[nh][nw] = True
        tree.union(f(h, w), f(nh, nw))
        if nh > 0 and chart[nh][nw] != chart[nh - 1][nw]:
            que.append((nh - 1, nw))
        if nh < H - 1 and chart[nh][nw] != chart[nh + 1][nw]:
            que.append((nh + 1, nw))
        if nw > 0 and chart[nh][nw] != chart[nh][nw - 1]:
            que.append((nh, nw - 1))
        if nw < W - 1 and chart[nh][nw] != chart[nh][nw + 1]:
            que.append((nh, nw + 1))

cntBW = defaultdict(lambda : [0, 0])

for h in range(H):
    for w in range(W):
        if tree.root(f(h, w)) == f(h, w) and chart[h][w] == '#':
            search(h, w)

for h in range(H):
    for w in range(W):
        if chart[h][w] == '#':
            cntBW[tree.root(f(h, w))][0] += 1
        else:
            cntBW[tree.root(f(h, w))][1] += 1

ans = 0

for black, white in cntBW.values():
    ans += black * white

print(ans)
