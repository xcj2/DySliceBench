class UnionFind():
    def __init__(self, n):
        self.size = n
        self.data = [-1 for _ in range(n)]
        self.sizes = [1 for _ in range(n)]

    def __len__(self):
        return self.size

    def root(self, i):
        """0 <= i < n"""
        if self.data[i] < 0:
            return i
        self.data[i] = self.root(self.data[i])
        return self.data[i]

    def connected(self, i, j):
        return self.root(i) == self.root(j)

    def groupsize(self, i):
        return self.sizes[self.root(i)]

    def roots(self):
        """O(n)"""
        return [i for i, v in enumerate(self.data) if v < 0]

    def unite(self, i, j):
        i = self.root(i)
        j = self.root(j)
        if i == j:
            return
        if (-self.data[i]) < (-self.data[j]):
            self.data[i] = j
            self.sizes[j] += self.sizes[i]
        elif (-self.data[i]) > (-self.data[j]):
            self.data[j] = i
            self.sizes[i] += self.sizes[j]
        else:
            self.data[i] += -1
            self.data[j] = i
            self.sizes[i] += self.sizes[j]


def nC2(n):
    return n * (n - 1) // 2


N, M = map(int, input().split())
AB = []
for _ in range(M):
    a, b = map(int, input().split())
    AB.append((a, b))

unconv = nC2(N)
revans = []
uf = UnionFind(N + 1)

for a, b in reversed(AB):
    revans.append(unconv)
    if uf.connected(a, b):
        continue
    unconv += nC2(uf.groupsize(a))
    unconv += nC2(uf.groupsize(b))
    uf.unite(a, b)
    unconv -= nC2(uf.groupsize(a))

for v in reversed(revans):
    print(v)
