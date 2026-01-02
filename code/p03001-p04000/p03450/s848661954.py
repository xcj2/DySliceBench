from collections import deque

class UnionFind :
    def __init__(self, size) :
        self.parent = list(range(size))
        self.height = [0] * size
        self.size = [1] * size
        self.component = size

    def root(self, index) :
        if self.parent[index] == index :  # 根の場合
            return index
        rootIndex = self.root(self.parent[index])  # 葉の場合親の根を取得
        self.parent[index] = rootIndex  # 親の付け直し
        return rootIndex

    def union(self, index1, index2) :  # 結合
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
        return self.root(index1) == self.root(index2)

    def sizeOfSameRoot(self, index) :
        return self.size[self.root(index)]

    def getComponent(self) :
        return self.component

N, M = map(int, input().split())

edges = [[] for _ in range(N + 1)]
tree = UnionFind(N + 1)
for _ in range(M):
    left, right, dist = map(int, input().split())
    edges[left].append((right, dist))
    edges[right].append((left, -dist))
    tree.union(left, right)

minDist = [None] * (N + 1)
for start in range(1, N + 1):
    if tree.root(start) != start:
        continue

    que = deque([(start, 0)])
    while que:
        now, dist = que.popleft()

        if minDist[now] == None:
            minDist[now] = dist
        else:
            if minDist[now] != dist:
                print('No')
                exit()
            continue

        for to, d in edges[now]:
            que.append((to, dist + d))

print('Yes')
