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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
    N,M = map(int, input().split())
    p_list = list(map(int, input().split()))

    uf = UnionFind(N)
    for i in range(M):
        x,y = map(int, input().split())
        uf.union(x-1,y-1)
        
    cnt = 0
    for i,p in enumerate(p_list):
        cnt += 1 if uf.same(p-1, i) else 0
    print(cnt)

if __name__ == "__main__":
    main()