N, M = [int(_) for _ in input().split()]
bridge = [[int(_) for _ in input().split()] for _ in range(M)]


class UnionFind:
    def __init__(self, N):
        self.par = [i for i in range(N + 1)]
        self.rank = [0] * (N + 1)
        self._number = [1] * (N + 1)

    def root(self, i):
        if self.par[i] == i:
            return i
        self.par[i] = self.root(self.par[i])
        return self.par[i]

    def same(self, i, j):
        return self.root(i) == self.root(j)

    def tree_rank(self, i):
        return self.rank[self.root(i)]

    def number(self, i):
        return self._number[self.root(i)]

    def union(self, i, j):
        _root_i = self.root(i)
        _root_j = self.root(j)
        if _root_i == _root_j:
            return
        else:
            if self.tree_rank(i) < self.tree_rank(j):
                self.par[_root_i] = _root_j
                self._number[_root_j] += self._number[_root_i]
            else:
                self.par[_root_j] = _root_i
                self._number[_root_i] += self._number[_root_j]
                if self.tree_rank(i) == self.tree_rank(j):
                    self.rank[_root_i] += 1


def whether_graph_connected(n, link):
    _islands = UnionFind(n)
    for l in link:
        _islands.union(l[0], l[1])
    return _islands.number(_islands.root(1)) == n

  
count = 0

for bridge_broken in bridge:
    bridge_remain = [_ for _ in bridge if _ != bridge_broken]
    if not whether_graph_connected(N, bridge_remain):
        count += 1

print(count)