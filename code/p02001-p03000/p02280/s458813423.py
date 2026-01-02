from sys import stdin

class Node:
    def __init__(self):
        self.parent = -1
        self.sibling = -1
        self.depth = -1
        self.height = -1
        self.children = [-1, -1]

class Tree:
    def __init__(self, nodes):
        self.nodes = nodes
        for i in range(self.size()):
            n = self.nodes[i]
            n.depth = self.depth(i)
            n.height = self.height(i)

    def depth(self, i):
        node = self.nodes[i]
        if self.isRoot(i):
            return 0
        else:
            return self.depth(node.parent)+1

    def height(self, i):
        node = self.nodes[i]
        if i == -1:
            return -1
        else:
            return max([self.height(c) for c in node.children])+1

    def size(self):
        return len(self.nodes)

    def isLeaf(self, i):
        return self.nodes[i].children == [-1, -1]

    def isRoot(self, i):
        return self.nodes[i].parent == -1

n = int(stdin.readline().rstrip())
nodes = [Node() for _ in range(n)]
for i in range(n):
    l = [int(x) for x in stdin.readline().rstrip().split()]
    nodes[l[0]].children = l[1:3]
    if l[1] != -1:
        nodes[l[1]].parent = l[0]
        nodes[l[1]].sibling = l[2]
    if l[2] != -1:
        nodes[l[2]].parent = l[0]
        nodes[l[2]].sibling = l[1]

t = Tree(nodes)
for i in range(t.size()):
    node = t.nodes[i]
    l = ["node ", i, ": parent = ", node.parent, ", sibling = ", node.sibling, ", degree = ", len([c for c in node.children if c != -1]), ", depth = ", node.depth, ", height = ", node.height, ", "]

    if t.isRoot(i):
        l.append("root")
    elif t.isLeaf(i):
        l.append("leaf")
    else:
        l.append("internal node")

    print(*l, sep="")
