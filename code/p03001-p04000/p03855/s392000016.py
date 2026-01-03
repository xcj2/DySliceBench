from collections import Counter
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if (root_x == root_y):
            return
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x

        elif self.rank[root_y] > self.rank[root_x]:
            self.parent[root_x] = root_y

        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1

    def isSame(self, x, y):
        return self.find(x) == self.find(y)

    def memsInGroup(self, x):
        """
        O(N)かかります
        """
        root = self.find(x)
        return [i for i in range(N) if root == self.find(i)]

    def sizeOfGroup(self, x):
        return len(self.memsInGroup(x))

N, K, L = map(int, input().split())

road = UnionFind(N)
train = UnionFind(N)

for i in range(K):
    p, q = map(int, input().split())
    road.unite(p-1, q-1)

for j in range(L):
    r, s = map(int, input().split())
    train.unite(r-1, s-1)

pair = [(road.find(i), train.find(i)) for i in range(N)]
# print(pair)
c = Counter(pair)
# print(c)
ans = [c[i] for i in pair]
# print(ans)
print(*ans)
