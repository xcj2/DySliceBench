import sys
from heapq import heappush, heappop

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.root[x] == x:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.root[x] = y
        else:
            self.root[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    

def kruskal(D, n):
    G = []
    UF = UnionFind(n)
    while len(D) > 0:
        cost, n1, n2 = heappop(D)

        if UF.is_same(n1, n2):
            continue
        else:
            G.append((cost, n1, n2))
            UF.unite(n1, n2)

    return G

def main():
    input = sys.stdin.readline
    N = int(input())
    C = []
    for i in range(N):
        x, y = map(int, input().split())
        C.append((i, x, y))

    X = sorted(C, key=lambda x: x[1])
    Y = sorted(C, key=lambda x: x[2])

    D = []
    for i in range(N-1):
        a, xa, _ = X[i]
        b, xb, _ = X[i+1]

        c, _, yc = Y[i]
        d, _, yd = Y[i+1]


        heappush(D, (xb - xa, a, b))
        heappush(D, (yd - yc, c, d))

    G = kruskal(D, N)
    ans = 0
    for g in G:
        ans += g[0]

    return ans


if __name__ == '__main__':
    print(main())
