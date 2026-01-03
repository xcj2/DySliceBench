N, k, l = map(int, input().split())

# UF木
class Uf:
    def __init__(self):
        self.Par = list(range(N + 1))

    def root(self, x):
        if self.Par[x] == x:
            return x
        else:
            self.Par[x] = self.root(self.Par[x])
            return self.Par[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            self.Par[x] = y


K = Uf()
L = Uf()
for i in range(k):
    K.unite(*map(int, input().split()))
for i in range(l):
    L.unite(*map(int, input().split()))
U = [[i, K.root(i), L.root(i)] for i in range(1, N+1)]
from operator import itemgetter
U.sort(key=itemgetter(1, 2))
i = 0
while i < N:
    n = 1
    while i+n < N:
        if U[i+n][1:3] == U[i][1:3]:
            n += 1
        else:
            break
    for j in range(n):
        U[i+j].append(n)
    i += n
U.sort(key=itemgetter(0))
A = [u[3] for u in U]
print(" ".join(map(str, A)))
