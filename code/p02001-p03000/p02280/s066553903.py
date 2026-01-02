class Tree:
    nodes = []
    def __init__(self):
        self.root = None
    def insert(self, nodenum, leftnum, rightnum):
        if leftnum != -1:
            self.nodes[nodenum].left = self.nodes[leftnum]
            self.nodes[leftnum].type_ = "internal node"
            self.nodes[leftnum].parent = self.nodes[nodenum]
            self.nodes[nodenum].degree += 1
        else:
            self.nodes[nodenum].left = -1
        if rightnum != -1:
            self.nodes[nodenum].right = self.nodes[rightnum]
            self.nodes[rightnum].type_ = "internal node"
            self.nodes[rightnum].parent = self.nodes[nodenum]
            self.nodes[nodenum].degree += 1
        else:
            self.nodes[nodenum].right = -1
        if leftnum != -1 and rightnum != -1:
            self.nodes[leftnum].sibling = rightnum
            self.nodes[rightnum].sibling = leftnum
    def depth(self, node):
        if node.left != -1:
            node.left.depth += node.depth + 1
            self.depth(node.left)
        if node.right != -1:
            node.right.depth += node.depth + 1
            self.depth(node.right)
    def height(self, node):
        if node.left == -1 and node.right == -1:
            node.type_ = "leaf"
            return 0
        elif node.left == -1:
            x = self.height(node.right)
            node.height = x + 1
            return x + 1
        elif node.right == -1:
            x = self.height(node.left)
            node.height = x + 1
            return x + 1
        else:
            x = max(self.height(node.left), self.height(node.right)) + 1
            node.height = x
            return x
class Node:
    def __init__(self, label, left = -1, right = -1):
        self.label = label
        self.type_ = "root"
        self.parent = -1
        self.sibling = -1
        self.depth = 0
        self.height = 0
        self.degree = 0
        self.left = left
        self.right = right

tree = Tree()
n = int(input())
for i in range(n):
    tree.nodes.append(Node(i))
for i in range(n):
    num, left, right = map(int, input().split())
    tree.insert(num, left, right)
for i in tree.nodes:
    if i.parent == -1:
        tree.depth(i)
        tree.height(i)
if n == 1:
    tree.nodes[0].type_ = "root"
for i in tree.nodes:
    print("node {0:}: parent = ".format(i.label), end = "")
    if i.parent == -1:
        print(i.parent, end = "")
    else:
        print(i.parent.label, end = "")
    print(", sibling = {0:}, degree = {1:}, depth = {2:}, height = {3:}, {4:}".format(i.sibling, i.degree, i.depth, i.height, i.type_))
