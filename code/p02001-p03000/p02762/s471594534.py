def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))

class UnionFind(object):

    def __init__(self, N):
        self.tree = [i for i in range(N)]
        self.rank = [0] * (N + 1)
        self.size = [1] * N  # 頂点iの属する連結成分の大きさ
        self.blocksize = [0] * N

    def find(self, x):
        if self.tree[x] == x:
            return x
        else:
            self.tree[x] = self.find(self.tree[x])  # 経路圧縮
            return self.tree[x]

    def block(self, x, y):
        if not self.has_same_parent(x, y):
            return
        self.blocksize[x] += 1
        self.blocksize[y] += 1

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        # ランクを考慮しない場合はどちらが親になっても良い
        if self.rank[x] < self.rank[y]:
            self.tree[x] = y
            self.size[y] += self.size[x]
        else:
            self.tree[y] = x
            self.size[x] += self.size[y]

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def has_same_parent(self, x, y):
        return self.find(x) == self.find(y)

    def component_size(self, x):
        return self.size[self.find(x)]


N, M, K = MI()
uf = UnionFind(N)
nl = [set() for _ in range(N)]
for _ in range(M):
    A, B = MI()
    nl[A - 1].add(B - 1)
    nl[B - 1].add(A - 1)
    uf.unite(A - 1, B - 1)

for _ in range(K):
    C, D = MI()
    uf.block(C - 1, D - 1)


ans = []
for i in range(N):
    a = uf.component_size(i) - len(nl[i]) - uf.blocksize[i] - 1
    ans.append(str(a))
print(' '.join(ans))