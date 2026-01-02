import sys, heapq
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

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

def kruskal(es, V):
    es.sort(key=lambda x:x[2])
    uf = UnionFind(V)
    res = 0
    for e in es:
        if not uf.same(e[0], e[1]):
            uf.union(e[0], e[1])
            res += e[2]
    return res

def resolve():
    V, E = LI()
    es = [[[]] for _ in range(E)]
    for i in range(E):
        s, t, w = LI()
        es[i] = [s, t, w]

    print(kruskal(es, V))

if __name__ == '__main__':
    resolve()
