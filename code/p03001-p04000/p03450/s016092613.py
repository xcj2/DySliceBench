class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.height = [0] * size
        self.size = [1] * size
        self.component = size

    def root(self, index):
        if self.parent[index] == index:  # 根の場合
            return index
        rootIndex = self.root(self.parent[index])  # 葉の場合親の根を取得
        self.parent[index] = rootIndex  # 親の付け直し
        return rootIndex

    def union(self, index1, index2):  # 結合
        root1 = self.root(index1)
        root2 = self.root(index2)

        if root1 == root2:  # 連結されている場合
            return

        self.component -= 1  # 連結成分を減らす

        if self.height[root1] < self.height[root2]:
            self.parent[root1] = root2  # root2に結合
            self.size[root2] += self.size[root1]
        else:
            self.parent[root2] = root1  # root1に結合
            self.size[root1] += self.size[root2]
            if self.height[root1] == self.height[root2]:
                self.height[root1] += 1
        return

    def isSameRoot(self, index1, index2):
        return self.root(index1) == self.root(index2)

    def sizeOfSameRoot(self, index):
        return self.size[self.root(index)]

    def getComponent(self):
        return self.component

N, M = map(int, input().split())
INF = 10**18
tree = UnionFind(N)

edges = [[] for _ in range(N)]
for _ in range(M):
    fr, to, d = map(int, input().split())
    fr -= 1
    to -= 1
    edges[to].append((fr, d))
    edges[fr].append((to, -d))
    tree.union(fr, to)

minDist = [INF] * N
for start in range(N):
    if tree.root(start) != start:
        continue
    st = [(start, 0)]
    while st:
        now, dist = st.pop()

        if minDist[now] == dist:
            continue

        if minDist[now] != INF and minDist[now] != dist:
            print('No')
            exit()
        minDist[now] = dist

        for to, d in edges[now]:
            if minDist[to] == d + dist:
                continue
            st.append((to, dist + d))

print('Yes')
