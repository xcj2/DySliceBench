# Binary Tree


class Node():
    def __init__(self, idx=-1, parent=-1, left=-1, right=-1):
        self.idx = idx
        self.parent = parent
        self.left = left
        self.right = right
        self.sibling = -1
        self.depth = -1
        self.height = -1
        self.type = None
        self.degree = -1


class BinaryTree():
    def __init__(self, n):
        self.T = [Node(i) for i in range(n)]

    def set_children(self, idx, l, r):
        node = self.T[idx]
        node.left = l
        node.right = r

        deg = 0
        if l != -1:
            deg += 1
            self.T[l].parent = idx
            self.T[l].sibling = r

        if r != -1:
            deg += 1
            self.T[r].parent = idx
            self.T[r].sibling = l

        node.degree = deg

    def get_root(self):
        for idx, node in enumerate(self.T):
            if node.parent == -1:
                return idx

    def set_type(self):
        for i, node in enumerate(self.T):
            if node.parent == -1:
                node.type = 'root'
            elif node.left == -1 and node.right == -1:
                node.type = 'leaf'
            else:
                node.type = 'internal node'

    def set_depth(self):
        root = self.get_root()
        self.set_depth_rec(root, 0)

    def set_depth_rec(self, idx, depth):
        node = self.T[idx]
        node.depth = depth
        if node.left != -1:
            self.set_depth_rec(node.left, depth+1)
        if node.right != -1:
            self.set_depth_rec(node.right, depth+1)

    def set_height(self):
        root = self.get_root()
        self.set_height_rec(root)

    def set_height_rec(self, idx):
        node = self.T[idx]
        if node.left == -1 and node.right == -1:
            node.height = 0
            return 0

        height = max(
            self.set_height_rec(node.left),
            self.set_height_rec(node.right)
        ) + 1

        node.height = height
        return height


N = int(input())
tree = BinaryTree(N)

for _ in range(N):
    idx, l, r = map(int, input().split())

    tree.set_children(idx, l, r)

tree.set_type()
tree.set_depth()
tree.set_height()

for node in tree.T:
    i = node.idx
    p = node.parent
    s = node.sibling
    deg = node.degree
    dep = node.depth
    h = node.height
    typ = node.type

    print(
        f'node {i}: parent = {p}, sibling = {s}, degree = {deg}, depth = {dep}, height = {h}, {typ}')

