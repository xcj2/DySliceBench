import sys
import pprint
sys.path.append('C:\\ARIHON')

# from Kraskal import compute_mst_kruskal
# import UnionFind
import array
import collections
from operator import itemgetter

class UnionFind(object):
 
    def __init__(self, number_of_nodes):  # 初期化
        self.par = array.array("L", range(number_of_nodes))
        self.rank = array.array("L", (0 for i in range(number_of_nodes)))
 
    def root(self, node):  # 根を求める
        if self.par[node] == node:
            return node
        else:
            r = self.root(self.par[node])
            self.par[node] = r  # 経路圧縮
            return r
 
    def in_the_same_set(self, node1, node2):  # 同じ集合に属するか
        return self.root(node1) == self.root(node2)
 
    def unite(self, node1, node2):  # 属する集合を併合
        x = self.root(node1)
        y = self.root(node2)
        if x == y:
            pass
        elif self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
 
 
# Kruskal法により最小全域木を求める
def compute_mst_kruskal(max_v, edges):
    edges.sort(key=lambda edge: edge.weight)
    uf = UnionFind(max_v)
    mst = []
    for edge in edges:
        if not uf.in_the_same_set(edge.start, edge.end):
            uf.unite(edge.start, edge.end)
            mst.append(edge)
    return mst
 
Edge = collections.namedtuple("Edge", "start end weight")

def main():
    n = int(input())
    l = []
    for i in range(n):
        x,y = map(int,input().split())
        l.append((x,y,i))
    
    edges = []

    lxsort = sorted(l,key=itemgetter(0))
    for i in range(n-1):
        edges.append(Edge(lxsort[i][2],lxsort[i+1][2],lxsort[i+1][0]-lxsort[i][0]))
    
    lysort = sorted(l,key=itemgetter(1))
    for i in range(n-1):
        edges.append(Edge(lysort[i][2],lysort[i+1][2],lysort[i+1][1]-lysort[i][1]))
    
    mst = compute_mst_kruskal(n,edges)

    print(sum(edge.weight for edge in mst))
 
if __name__ == '__main__':
    main()