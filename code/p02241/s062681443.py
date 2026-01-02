import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

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

    def unite(self, x, y):
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

def kruskal(es, V):
    es.sort(key=lambda x:x[2])
    uf = UnionFind(V)
    res = 0
    for e in es:
        if not uf.same(e[0], e[1]):
            uf.unite(e[0], e[1])
            res += e[2]
    return res

def resolve():
    n = I()
    es = []
    for i in range(n):
        a = LI()
        for j in range(n):
            if a[j]!=-1:
                es.append((i, j, a[j]))

    ans = kruskal(es, n)
    print(ans)

if __name__ == '__main__':
    resolve()

