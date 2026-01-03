import sys
from heapq import heappush, heappop

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.size = [1] * (n+1)  # The number of nodes under the target node.
        self.weight = [0] * (n+1)  # Distance from the root

    def find(self, x):
        if self.root[x] == x:
            return x
        else:
            y = self.find(self.root[x])
            self.weight[x] += self.weight[self.root[x]]
            self.root[x] = y
            return self.root[x]

    def unite(self, x, y, w=0):
        rx = self.find(x)
        ry = self.find(y)
        if self.rank[rx] < self.rank[ry]:
            self.root[rx] = ry
            self.size[ry] += self.size[rx]
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            self.root[ry] = rx
            self.size[rx] += self.size[ry]
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    
    def diff(self, x, y):
        return self.weight[y] - self.weight[x]


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
