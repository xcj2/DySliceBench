class Tree:
    def __init__(self, ary):
        self.nodes = [
            Node(node, self) for node in sorted(ary, key=lambda x: x[0])
        ]
        [node.set() for node in self.nodes]
        for node in self.nodes:
            if node.parent == -1:
                self.root = node
                break
        self.root.set_depth(0)
        self.root.set_height()

    def output(self):
        [node.output() for node in self.nodes]

    def preorder(self):
        print('Preorder')
        self.root.preorder()
        print()

    def inorder(self):
        print('Inorder')
        self.root.inorder()
        print()

    def postorder(self):
        print('Postorder')
        self.root.postorder()
        print()


class Node:
    def __init__(self, node, tree):
        self.tree = tree
        self.no = node[0]
        self.left = node[1]
        self.right = node[2]
        self.parent = -1
        self.sibling = -1
        self.degree = 0

    def set(self):
        if self.left > -1:
            self.tree.nodes[self.left].parent = self.no
            if self.right > -1:
                self.tree.nodes[self.right].sibling = self.left
            self.degree += 1

        if self.right > -1:
            self.tree.nodes[self.right].parent = self.no
            if self.left > -1:
                self.tree.nodes[self.left].sibling = self.right
            self.degree += 1

    def set_depth(self, d):
        self.depth = d
        if self.left > -1:
            self.tree.nodes[self.left].set_depth(d + 1)
        if self.right > -1:
            self.tree.nodes[self.right].set_depth(d + 1)

    def set_height(self):
        if self.degree == 0:
            self.height = 0
        else:
            self.tree.nodes[self.right].set_height()
            self.tree.nodes[self.left].set_height()
            self.height = 1 + max(self.tree.nodes[self.right].height,
                                  self.tree.nodes[self.left].height)

    def output(self):
        if self.parent == -1:
            kind = 'root'
        elif self.degree == 0:
            kind = 'leaf'
        else:
            kind = 'internal node'
        print(
            'node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.
            format(self.no, self.parent, self.sibling, self.degree, self.depth,
                   self.height, kind))

    def preorder(self):
        print(' {}'.format(self.no), end='')
        if self.left > -1:
            self.tree.nodes[self.left].preorder()
        if self.right > -1:
            self.tree.nodes[self.right].preorder()

    def inorder(self):
        if self.left > -1:
            self.tree.nodes[self.left].inorder()
        print(' {}'.format(self.no), end='')
        if self.right > -1:
            self.tree.nodes[self.right].inorder()

    def postorder(self):
        if self.left > -1:
            self.tree.nodes[self.left].postorder()
        if self.right > -1:
            self.tree.nodes[self.right].postorder()
        print(' {}'.format(self.no), end='')


n = int(input())
ary = [[int(_) for _ in input().split()] for i in range(n)]
tree = Tree(ary)
tree.preorder()
tree.inorder()
tree.postorder()

