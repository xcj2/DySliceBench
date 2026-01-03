import sys
sys.setrecursionlimit(1000000)

class UnionFind:
    def __init__(self, n: int) -> None:
        #マイナスならルートでその深さを表す。プラスならルートのノードを指す。
        self.nodes = [-1]*n
 
    def find_root(self, x: int) -> int:
        if self.nodes[x] < 0:
            return x
        else:
            self.nodes[x] = self.find_root(self.nodes[x])
            return self.nodes[x]
 
    def unite(self, x: int, y: int) -> None:
        x, y = self.find_root(x), self.find_root(y)
        #浅い方につなぐ
        if (x != y):
            if (x < y):
                self.nodes[y] += self.nodes[x]
                self.nodes[x] = y
            else:
                self.nodes[x] += self.nodes[y]
                self.nodes[y] = x
        
    def is_same(self, x: int, y: int) -> bool:
        return self.find_root(x) == self.find_root(y)

from operator import itemgetter

N = int(input())
G = [[i] + list(map(int, input().split())) for i in range(N)]

#X,Yそれぞれでソートして各都市の最短距離を求める
G_sorted_by_x = sorted(G, key=itemgetter(1))
G_sorted_by_y = sorted(G, key=itemgetter(2))
R = []
for i in range(N-1):
    i0, x0, _ = G_sorted_by_x[i]
    i1, x1, _ = G_sorted_by_x[i+1]
    R.append((x1-x0, i0, i1))
    i0, _, y0 = G_sorted_by_y[i]
    i1, _, y1 = G_sorted_by_y[i+1]
    R.append((y1-y0, i0, i1))

R_sorted_by_cost = sorted(R, key=itemgetter(0))

#print(R_sorted_by_cost)

uf = UnionFind(N)
total_cost = 0
for cost, i, j in R_sorted_by_cost:
    if (not uf.is_same(i, j)):
        uf.unite(i, j)
        total_cost += cost
    #print((cost, i, j))
print(total_cost)
