class Tree:
    def __init__(self, ary):
        self.nodes = [
            Node(node, self) for node in sorted(ary, key=lambda x: x[0])
        ]
        [node.set() for node in self.nodes]
        for node in self.nodes:
            if node.parent == -1:
                node.set_depth(0)
                break

    def output(self):
        [node.output() for node in self.nodes]


class Node:
    def __init__(self, node, tree):
        self.tree = tree
        self.no = node[0]
        self.parent = -1
        self.right = False
        self.left = False
        self.children = node[2:]

    def set(self):
        if self.children:
            for i, child in enumerate(self.children):
                self.tree.nodes[child].parent = self.no
                if i < len(self.children) - 1:
                    self.tree.nodes[child].right = self.children[i + 1]
                self.left = self.children[0]

    def set_depth(self, d):
        self.depth = d
        if type(self.right) != bool:
            self.tree.nodes[self.right].set_depth(d)
        if type(self.left) != bool:
            self.tree.nodes[self.left].set_depth(d + 1)

    def output(self):
        if self.parent == -1:
            kind = 'root'
        elif not self.children:
            kind = 'leaf'
        else:
            kind = 'internal node'

        print('node {}: parent = {}, depth = {}, {}, {}'.format(
            self.no, self.parent, self.depth, kind, self.children))


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10 ** 6)

    n = int(input())
    ary = [[int(_) for _ in line.strip().split()] for line in sys.stdin]
    # ary = [[int(_) for _ in input().split()] for i in range(n)]
    tree = Tree(ary)
    tree.output()

