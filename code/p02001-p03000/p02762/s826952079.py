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
    N, M, K = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    friends = [0 for _ in range(N)]
    blocks = [0 for _ in range(N)]
    unions = UnionFind(N)
    for a, b in AB:
        unions.union(a-1, b-1)
        friends[a-1] += 1
        friends[b-1] += 1
    for c, d in CD:
        if unions.same(c-1, d-1):
            blocks[c-1] += 1
            blocks[d-1] += 1
    ans = []
    for i in range(N):
        ans.append(unions.size(i)-friends[i]-blocks[i]-1)
    print(*ans)


if '__main__' == __name__:
    resolve()
