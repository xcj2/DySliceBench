class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n 

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


def resolve():
    N, M = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for i in range(M)]
    cnt = 0
    for i in range(len(AB)):
        uf = UnionFind(N)
        for edge in AB[:i]+AB[i+1:]:
            uf.union(edge[0]-1, edge[1]-1)
        if uf.find(AB[i][0]-1) != uf.find(AB[i][1]-1):
            cnt += 1
    print(cnt)


if '__main__' == __name__:
    resolve()