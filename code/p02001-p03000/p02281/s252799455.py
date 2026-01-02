from sys import stdin

class Node:
    def __init__(self):
        self.parent = -1
        self.children = [-1, -1]

class Tree:
    def __init__(self, nodes):
        self.nodes = nodes

    def size(self):
        return len(self.nodes)

    def preorder(self, i):
        if i != -1:
            c = self.nodes[i].children
            print(" ", i, sep="", end="")
            self.preorder(c[0])
            self.preorder(c[1])

    def inorder(self, i):
        if i != -1:
            c = self.nodes[i].children
            self.inorder(c[0])
            print(" ", i, sep="", end="")
            self.inorder(c[1])

    def postorder(self, i):
        if i != -1:
            c = self.nodes[i].children
            self.postorder(c[0])
            self.postorder(c[1])
            print(" ", i, sep="", end="")

n = int(stdin.readline().rstrip())
nodes = [Node() for _ in range(n)]
for i in range(n):
    l = [int(x) for x in stdin.readline().rstrip().split()]
    nodes[l[0]].children = l[1:3]
    if l[1] != -1:
        nodes[l[1]].parent = l[0]
    if l[2] != -1:
        nodes[l[2]].parent = l[0]

t = Tree(nodes)

root = [node.parent for node in t.nodes].index(-1)
print("Preorder")
t.preorder(root)
print("\nInorder")
t.inorder(root)
print("\nPostorder")
t.postorder(root)
print()

