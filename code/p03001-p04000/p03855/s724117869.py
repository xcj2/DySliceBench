from collections import Counter

# UnionFind
class UnionFind():

    #0~Nまでの頂点数で初期化していることに注意
    def __init__(self, n):
        self.n = n
        self.root = [-1] * n

    def FindRoot(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.FindRoot(self.root[x])
            return self.root[x]

    def Unite(self, x, y):
        x = self.FindRoot(x)
        y = self.FindRoot(y)

        if x == y:
            return False
        if self.Size(x) < self.Size(y):
            x, y = y, x
        self.root[x] += self.root[y]
        self.root[y] = x

        return True

    def isSameGroup(self, x, y):
        return self.FindRoot(x) == self.FindRoot(y)

    def Size(self, x):
        return -self.root[self.FindRoot(x)]

N, K, L = map(int, input().split())

Uni1 = UnionFind(N)

for _ in range(K):
    p, q = map(int, input().split())
    Uni1.Unite(p-1, q-1)

Uni2 = UnionFind(N)

for _ in range(L):
    r, s = map(int, input().split())
    Uni2.Unite(r-1, s-1)

pair = []
for i in range(N):
    pair.append((Uni1.FindRoot(i), Uni2.FindRoot(i)))

c = Counter(pair)
cnt = []
for i in range(N):
    cnt.append(c[pair[i]])

print(*cnt)
