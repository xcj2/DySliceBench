import sys
from pprint import pprint


class UnionFind:
    def __init__(self):
        self._parent = {}
        self._rank = {}
        self._equiv = {}
    
    def _find(self, x):
        if self._parent[x] == x:
            return self._parent[x]
        else:
            p = self._find(self._parent[x])
            self._parent[x] = p
            return p
    
    def _set_parent(self, child, parent):
        self._parent[child] = parent
        self._equiv[parent].update(self._equiv.pop(child))
    
    def _union(self, x, y):
        x = self._find(x)
        y = self._find(y)
        if x == y: return
        if self._rank[x] > self._rank[y]:
            self._set_parent(y, x)
        elif  self._rank[x] < self._rank[y]:
            self._set_parent(x, y)
        else:
            self._set_parent(x, y)
            self._rank[x] += 1
    
    def _make_set(self, x):
        self._parent[x] = x
        self._rank[x] = 0
        self._equiv[x] = {x}
    
    def unite(self, *elements):
        if not elements: return
        for x in elements:
            if x in self._parent: continue
            self._make_set(x)
        x0 = elements[0]
        for x in elements[1:]:
            self._union(x0, x)
    
    def groups(self):
        return [set(e) for e in self._equiv.values()]


def pairs(ncol, nrow):
    # ?????????
    for x in range(ncol - 1):
        for y in range(nrow):
            yield [(x, y), (x + 1, y)]

    # ?????????
    for x in range(ncol):
        for y in range(nrow - 1):
            yield [(x, y), (x, y + 1)]

    # ???????????????
    for x in range(ncol - 1):
        for y in range(nrow - 1):
            yield [(x, y), (x + 1, y + 1)]

    # ???????????????
    for x in range(ncol - 1):
        for y in range(1, nrow):
            yield [(x, y), (x + 1, y - 1)]


def solve(ncol, nrow, rows):
 
    f = UnionFind()
    for x in range(ncol):
        for y in range(nrow):
            if rows[y][x]:
                f.unite((x, y))
    for (x1, y1), (x2, y2) in pairs(ncol, nrow):
        if rows[y1][x1] and rows[y2][x2]:
            f.unite((x1, y1), (x2, y2))
    return len(f.groups())


def main():
    while True:
        ncol, nrow = map(int, input().split())
        if ncol == 0 and nrow == 0:
            break
        rows = []
        for _ in range(nrow):
            row = list(map(int, input().split()))
            rows.append(row)
        print(solve(ncol, nrow, rows))

main()