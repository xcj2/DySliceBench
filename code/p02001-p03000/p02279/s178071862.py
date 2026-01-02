class Tree:
    nodes = []
    def __init__(self, root = None):
        None
    def insert(self, label, children = []):
        if children != []:
            for i in children:
                self.nodes[label].children.append(self.nodes[i])
                self.nodes[i].parent = self.nodes[label]
                self.nodes[i].type_ = "internal node"
    def depth(self, node):
        if node.children == []:
            node.type_ = "leaf"
        else:
            for i in node.children:
                i.depth = node.depth + 1
                self.depth(i)

class Node:
    def __init__(self, label, children = []):
        self.label = label
        self.type_ = "root"
        self.depth = 0
        self.parent = -1
        self.children = [] # self.children = childrenにするとハマる

tree = Tree()
n = int(input())
for i in range(n):
    tree.nodes.append(Node(i))
for i in range(n):
    children = []
    label, num, *children = map(int, input().split())
    tree.insert(label, children)
for i in tree.nodes:
    if i.parent == -1:
        tree.depth(i)
        None
if n == 1:
    tree.nodes[0].type_ = "root"
for i in tree.nodes:
    print("node {0:}: parent = {1:}, depth = {2:}, {3:}, ".\
            format(i.label, i.parent if i.parent == -1 else i.parent.label,\
            i.depth, i.type_), end = "")
    print([i.label for i in i.children])
