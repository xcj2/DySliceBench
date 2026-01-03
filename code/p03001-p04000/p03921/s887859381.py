import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from functools import reduce

class UnionFind:
    def __init__(self, node: int) -> None:
        self.n = node
        self.par = [i for i in range(self.n)]
        self.rank = [0 for i in range(self.n)]

    def find(self, x: int) -> int:
        if x == self.par[x]:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x: int, y: int) -> bool:
        if self.isSame(x, y):
            # print("x and y has already united")
            return False

        rx = self.find(x)
        ry = self.find(y)

        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = self.par[ry]
        else:
            self.par[ry] = self.par[rx]

            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

        return True

    def isSame(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


n, m = li()
lang = [[] for _ in range(m)]
for person in range(n):
    kl = list(li_())
    for langi in kl[1:]:
        lang[langi].append(person)

uf = UnionFind(n)
for langi in lang:
    if len(langi) < 2:
        continue

    for i in range(len(langi)-1):
        uf.unite(langi[i], langi[i+1])


for i in range(n):
    uf.find(i)

ok = True
for i in range(1, n):
    if uf.isSame(0, i):
        continue

    else:
        ok = False
        break

print("YES" if ok else "NO")