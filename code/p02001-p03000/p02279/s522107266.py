from sys import stdin

class Node:
    def __init__(self):
        self.parent = -1
        self.depth = -1
        self.children = []

class Tree:
    def __init__(self, nodes):
        self.nodes = nodes

        for i in range(self.size()):
            if not self.isLeaf(i):
                for c in self.nodes[i].children:
                    self.nodes[c].parent = i

        for i in range(self.size()):
            self.nodes[i].depth = self.depth(i)

    def depth(self, i):
        n = self.nodes[i]
        if self.isRoot(i):
            return 0
        else:
            return self.depth(n.parent)+1


    def size(self):
        return len(self.nodes)

    def isLeaf(self, i):
        return len(self.nodes[i].children) == 0

    def isRoot(self, i):
        return self.nodes[i].parent == -1

n = int(stdin.readline().rstrip())
nodes = [Node() for _ in range(n)]
for i in range(n):
    l = [int(x) for x in stdin.readline().rstrip().split()]
    if l[1] > 0:
        nodes[l[0]].children.extend(l[2:])

t = Tree(nodes)
for i in range(t.size()):
    l = ["node ", i, ": parent = ", t.nodes[i].parent, ", depth = ", t.nodes[i].depth, ", "]
    if t.isRoot(i):
        l.append("root, ")
    elif t.isLeaf(i):
        l.append("leaf, ")
    else:
        l.append("internal node, ")

    l.append(t.nodes[i].children)
    print(*l, sep="")
