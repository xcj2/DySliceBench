import sys
input = sys.stdin.readline

class LCA(object):
    def __init__(self, n, root, edges, decrement=True):
        """
        :param n: 頂点数
        :param root: 木の根
        :param edges: 辺のリスト
        :param decrement:

        :param self.depth: rootを根とした時の各頂点の深さ
        """
        self.n = n
        self.decrement = decrement
        self.root = root - self.decrement
        self.edges = [set() for _ in range(self.n)]
        i = 0
        for x, y in edges:
            self.add_edge(x,y,i)
            i += 1
        self.k_max = (self.n - 1).bit_length()
        self.depth = [-1 if i != self.root else 0 for i in range(self.n)]
        self.doubling = [[-1] * self.n for _ in range(self.k_max)]
        self.path_bit = [-1]*self.n
        self.dfs()
        for i in range(1, self.k_max):
            for k in range(self.n):
                if self.doubling[i - 1][k] != -1:
                    self.doubling[i][k] = self.doubling[i - 1][self.doubling[i - 1][k]]

    def add_edge(self, x, y, i):
        """
        後から追加した場合は update() をする
        """
        if self.decrement:
            x -= 1
            y -= 1
        self.edges[x].add((y,i))
        self.edges[y].add((x,i))

    def dfs(self):
        next_set = [self.root]
        self.path_bit[self.root] = 0
        while next_set:
            p = next_set.pop()
            for q, i in self.edges[p]:
                if self.depth[q] == -1:
                    self.depth[q] = self.depth[p] + 1
                    self.path_bit[q] = self.path_bit[p] | 1 << i
                    self.doubling[0][q] = p
                    next_set += [q]

    def get_list(self, u, v):
        if self.decrement:
            u -= 1
            v -= 1
        return self.path_bit[u] ^ self.path_bit[v]

    def draw(self):
        """
        :return: グラフを可視化
        """
        import matplotlib.pyplot as plt
        import networkx as nx

        G = nx.Graph()
        for x in range(self.n):
            for y in self.edges[x]:
                G.add_edge(x + self.decrement, y + self.decrement)

        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos)
        plt.axis("off")
        plt.show()

#################################################################################################

from itertools import combinations

def popcnt(n):
    c = (n & 0x5555555555555555) + ((n>>1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c>>2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c>>4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c>>8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c>>16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c>>32) & 0x00000000ffffffff)
    return c

N = int(input())
edges = []
for _ in range(N-1):
    x, y = map(int, input().split())
    edges.append((x,y))

lca = LCA(N, 1, edges, decrement=True)

M = int(input())
edges2 = []
for _ in range(M):
    x, y = map(int, input().split())
    edges2.append((x,y))

res = pow(2,N-1)
for m in range(1,M+1):
    for a in combinations(edges2, m):
        temp = 0
        for b in a:
            temp |= lca.get_list(*b)
        res += (1-2*(m%2))*pow(2,N -1 - popcnt(temp))

print(res)