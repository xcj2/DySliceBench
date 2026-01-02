from collections import deque

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.height = [0] * size
        self.size = [1] * size
        self.componentCount = size

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

        self.componentCount -= 1  # 連結成分を減らす

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

H, W = map(int, input().split())
C = tuple(map(int, input().split()))
D = tuple(map(int, input().split()))
S = [input() for _ in range(H)]

def cord(h, w):
    return h * W + w

tree = UnionFind(H * W + 100)

for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            continue

        for dh, dw in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            toH, toW = h + dh, w + dw

            if 0 <= toH < H and 0 <= toW < W and S[toH][toW] == '.':
                tree.union(cord(h, w), cord(toH, toW))

roots = [tree.root(i) for i in range(H * W)]
M = max(roots) + 1
edges = [set() for _ in range(M)]

def search(h, w):
    for dh in range(-2, 3):
        for dw in range(-2, 3):
            toH, toW = h + dh, w + dw
            if 0 <= toH < H and 0 <= toW < W and S[toH][toW] == '.':
                if roots[cord(h, w)] == roots[cord(toH, toW)]:
                    continue
                edges[roots[cord(h, w)]].add(roots[cord(toH, toW)])

for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            continue
        search(h, w)

edges = [list(e) for e in edges]

S = roots[cord(C[0] - 1, C[1] - 1)]
T = roots[cord(D[0] - 1, D[1] - 1)]

INF = 10**18
que = deque([(S, 0)])
minDist = [INF] * M
minDist[S] = 0

while que:
    now, dist = que.popleft()

    for to in edges[now]:
        if minDist[to] > dist + 1:
            minDist[to] = dist + 1
            que.append((to, dist + 1))

print(minDist[T] if minDist[T] < INF else -1)
