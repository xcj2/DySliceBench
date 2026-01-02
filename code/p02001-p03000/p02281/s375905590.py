# Tree Walk
class Tree:
    nodes = []
    def __init__(self):
        self.root = None
    def insert(self, nodenum, leftnum, rightnum):
        if leftnum != -1:
            self.nodes[nodenum].left = self.nodes[leftnum]
            self.nodes[leftnum].parent = self.nodes[nodenum]
        if rightnum != -1:
            self.nodes[nodenum].right = self.nodes[rightnum]
            self.nodes[rightnum].parent = self.nodes[nodenum]
    def preorder_walk(self, node):
        if node == -1:
            return
        print("", node.label, end = "")
        self.preorder_walk(node.left)
        self.preorder_walk(node.right)
    def inorder_walk(self, node):
        if node == -1:
            return
        self.inorder_walk(node.left)
        print("", node.label, end = "")
        self.inorder_walk(node.right)
    def postorder_walk(self, node):
        if node == -1:
            return
        self.postorder_walk(node.left)
        self.postorder_walk(node.right)
        print("", node.label, end = "")

class Node:
    def __init__(self, label):
        self.label = label
        self.parent = -1
        self.left = -1
        self.right = -1

tree = Tree()
n = int(input())
for i in range(n):
    tree.nodes.append(Node(i))
for i in range(n):
    num, left, right = map(int, input().split())
    tree.insert(num, left, right)
for i in tree.nodes:
    if i.parent == -1:
        print("Preorder")
        tree.preorder_walk(i)
        print("")
        print("Inorder")
        tree.inorder_walk(i)
        print("")
        print("Postorder")
        tree.postorder_walk(i)
        print("")
