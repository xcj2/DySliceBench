# Acceptance of input

import sys

file_input = sys.stdin

v_num, e_num = map(int, file_input.readline().split())

E = []
for line in file_input:
    s, t, w = map(int, line.split())
    E.append((w, s, t))


# Disjoint Set: Union Find Tree

# Implementation of disjoint sets by tree
# Compression of the path
# merge smaller tree to large tree

class DisjointSets:
    def __init__(self, size):
        # negative values are roots(representatives of each tree)
        # positive values represent the parent element
        self.table = [-1 for _ in range(size)]

    def _find(self, x):
        if self.table[x] < 0:
            return x
        else:
            # compression of the path
            self.table[x] = self._find(self.table[x])
            return self.table[x]

    def uniteSets(self, x, y):
        s1 = self._find(x)
        s2 = self._find(y)
        if s1 != s2:
            if self.table[s1] < self.table[s2]: # the smaller has more elements
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2

    def isDisjoint(self, x, y):
        if self._find(x) != self._find(y):
            return True
        else:
            return False


# Kruskal's algorithm

def kruskal(vertices_num, edges):
    edges.sort(reverse = True)
    S = DisjointSets(vertices_num)
    weight = 0

    while edges:
        w, s, t = edges.pop()
        if S.isDisjoint(s, t):
            S.uniteSets(s, t)
            weight += w

    print(weight)


# Output

kruskal(v_num, E)