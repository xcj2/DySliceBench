# -*- coding: utf-8 -*-
# abc126/abc126_e
import sys

s2nn = lambda s: [int(c) for c in s.split(' ')]
ss2nn = lambda ss: [int(s) for s in list(ss)]
ss2nnn = lambda ss: [s2nn(s) for s in list(ss)]
i2s = lambda: sys.stdin.readline().rstrip()
i2n = lambda: int(i2s())
i2nn = lambda: s2nn(i2s())
ii2ss = lambda n: [i2s() for _ in range(n)]
ii2nn = lambda n: ss2nn(ii2ss(n))
ii2nnn = lambda n: ss2nnn(ii2ss(n))


class UnionFindNode(object):
    def __init__(self, group_id, parent=None, value=None):
        self._group_id = group_id
        self._parent = parent
        self.value = value
        self._rank = 1
    
    def __str__(self):
        template = "UnionFindNode(group_id: {}, \n\tparent: {}, value: {}, size: {})"
        return template.format(self._group_id, self._parent, self.value, self._rank)
    
    def is_root(self):
        return not self._parent
    
    def root(self):
        parent = self
        while not parent.is_root():
            parent = parent._parent
            self._parent = parent
        return parent
    
    def find(self):
        root = self.root()
        return root._group_id
    
    def rank(self):
        root = self.root()
        return root._rank

    def unite(self, unite_node):
        root = self.root()
        unite_root = unite_node.root()

        if root._group_id != unite_root._group_id:
            if root.rank() > unite_root.rank():
                unite_root._parent = root
                root._rank = max(root._rank, unite_root._rank + 1)
            else:
                root._parent = unite_root
                unite_root._rank = max(root._rank + 1, unite_root._rank)

def main():
    N, M = i2nn()
    A = [UnionFindNode(x, value=x) for x in range(N)]
    s = 0
    for i in range(M):
        x, y, z = i2nn()
        A[x-1].unite(A[y-1])
    for a in A:
        s += int(a.is_root())
    print(s)
    return

main()