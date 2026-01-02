from sys import stdin

class Node(object):
    def __init__(self, parent=None, left=None, right=None,
                 name=None, sibling=None, degree=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.name = name
        self.sibling = sibling
        self.degree = degree

def print_nodes(nodes, n):
    def get_depth(nodes, u):
        p = nodes[u].parent
        nonlocal d
        if p != None and p != -1:
            get_depth(nodes, p)
            d += 1
        return d

    def get_height(nodes, u):
        h1 = 0
        h2 = 0
        r = nodes[u].right
        l = nodes[u].left
        if r != -1:
            h1 = get_height(nodes, r) + 1
        if l != -1:
            h2 = get_height(nodes, l) + 1
        return max(h1, h2)

    for i in range(n):
        d = 0
        if nodes[i].parent == None:
            nodes[i].parent = -1
            nodes[i].sibling = -1
            nodes[i].name = "root"
        print("node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}".format(
               i, nodes[i].parent, nodes[i].sibling, nodes[i].degree, get_depth(nodes, i),
               get_height(nodes, i), nodes[i].name))

def read_binary_tree(nodes, n):
    for _ in range(n):
        i = [int(i) for i in stdin.readline().strip().split()]
        nodes[i[0]].left = i[1]
        nodes[i[0]].right = i[2]
        nodes[i[0]].degree = 0
        if i[1] != -1:
            nodes[i[0]].name = "internal node"
            nodes[i[1]].parent = i[0]
            nodes[i[1]].sibling = i[2]
            nodes[i[0]].degree += 1
        if i[2] != -1:
            nodes[i[0]].name = "internal node"
            nodes[i[2]].parent = i[0]
            nodes[i[2]].sibling = i[1]
            nodes[i[0]].degree += 1
        if i[1] == -1 and i[2] == -1:
            nodes[i[0]].name = "leaf"

n = int(input())
nodes = [Node() for _ in range(n)]
read_binary_tree(nodes, n)
print_nodes(nodes, n)
