class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # 要素xの根の値を取得
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def resolve():
    N, M = list(map(int, input().split()))
    P = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    uf = UnionFind(N)
    for xy in XY:
        uf.union(xy[0]-1, xy[1]-1)
    cnt = 0
    for i in range(N):
        if uf.same(i, P[i]-1):
            cnt += 1

    print(cnt)
    
    
if '__main__' == __name__:
    resolve()