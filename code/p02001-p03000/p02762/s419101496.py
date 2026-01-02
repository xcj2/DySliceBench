from bisect import bisect_left


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parent = [-1 for _ in range(n)]
        # 正==子: 根の頂点番号 / 負==根: 連結頂点数

    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        else:
            if self.size(x) < self.size(y):
                x, y = y, x
            self.parent[x] += self.parent[y]
            self.parent[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        x = self.find(x)
        return -self.parent[x]

    def is_root(self, x):
        return self.parent[x] < 0

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]


def check(i, j):
    global friends
    global blocks
    a = bisect_left(friends, [i, j])
    b = bisect_left(friends, [j, i])
    c = bisect_left(blocks, [i, j])
    d = bisect_left(blocks, [j, i])



n, m, k = map(int, input().split())

blocks = [[] for _ in range(n)]
friend_num = [0] * n
uf = UnionFind(n)

for _ in range(m):
    array = list(map(int, input().split()))
    uf.unite(array[0]-1, array[1]-1)
    friend_num[array[0]-1] += 1
    friend_num[array[1]-1] += 1

for _ in range(k):
    array = list(map(int, input().split()))
    blocks[array[0]-1].append(array[1]-1)
    blocks[array[1]-1].append(array[0]-1)

for i in range(n):
    uf.find(i)

for i in range(n):
    num = uf.size(i)
    personal_block_list = blocks[i]
    personal_block_num = 0
    for j in personal_block_list:
        if uf.same(i, j):
            personal_block_num += 1

    print(num-friend_num[i]-personal_block_num-1, end=' ')


