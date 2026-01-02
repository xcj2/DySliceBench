import sys
sys.setrecursionlimit(10**6)


class Node():
    def __init__(self, parent=-1, child=-1, sibling=-1, depth=-1):
        self.parent = parent
        self.first_child = child
        self.next_sibling = sibling
        self.depth = depth


class Tree():
    def __init__(self, n):
        self.T = [Node() for _ in range(n)]

    def type_of(self, i):
        node = self.T[i]
        if node.parent == -1:
            return 'root'
        if node.first_child == -1:
            return 'leaf'
        return 'internal node'

    def children_of(self, i):
        node = self.T[i]
        if node.first_child == -1:
            return []

        children = [node.first_child]
        node = self.T[node.first_child]
        while node.next_sibling != -1:
            children.append(node.next_sibling)
            node = self.T[node.next_sibling]

        return children

    def depth_of(self, i):
        return self.T[i].depth

    def get_root(self, ):
        for i, node in enumerate(self.T):
            if node.parent == -1:
                return i

    def set_children(self, i, c):

        if len(c) == 0:
            return False

        self.T[i].first_child = c[0]

        num_c = len(c)
        for j in range(num_c-1):
            self.T[c[j]].parent = i
            self.T[c[j]].next_sibling = c[j+1]
        self.T[c[num_c-1]].parent = i

        return True

    def set_depth(self, ):
        root = self.get_root()
        self.depth(root, 0)

    def depth(self, i, d):
        self.T[i].depth = d
        if self.T[i].next_sibling != -1:
            self.depth(self.T[i].next_sibling, d)
        if self.T[i].first_child != -1:
            self.depth(self.T[i].first_child, d+1)

    def parent_of(self, i):
        return self.T[i].parent


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
T = Tree(N)

for i, *c in A:
    c = c[1:]
    T.set_children(i, c)
T.set_depth()

for i in range(N):
    p = T.parent_of(i)
    d = T.depth_of(i)
    t = T.type_of(i)
    c = T.children_of(i)
    print(f'node {i}: parent = {p}, depth = {d}, {t}, {c}')

