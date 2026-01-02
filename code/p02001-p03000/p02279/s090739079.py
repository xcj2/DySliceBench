from sys import stdin

class Node(object):
    def __init__(self, parent=None, children=None, name=None):
        self.parent = parent
        self.children = children
        self.name = name

def print_nodes(nodes, n):
    def get_depth(nodes, u):
        p = nodes[u].parent
        nonlocal d
        if p != None and p != -1:
            get_depth(nodes, p)
            d += 1
        return d

    for i in range(n):
        d = 0
        if nodes[i].parent == None:
            nodes[i].parent = -1
            nodes[i].name = "root"
        print("node {0}: parent = {1}, depth = {2}, {3}, {4}".format(
               i, nodes[i].parent, get_depth(nodes, i), nodes[i].name, nodes[i].children))

def read_rooted_tree(nodes, n):
    for _ in range(n):
        i = [int(i) for i in stdin.readline().strip().split()]
        c = i[2:len(i)]
        nodes[i[0]].children = c
        if c:
            nodes[i[0]].name = "internal node"
        else:
            nodes[i[0]].name = "leaf"
        for j in nodes[i[0]].children:
            nodes[j].parent = i[0]

n = int(input())
nodes = [Node() for _ in range(n)]
read_rooted_tree(nodes, n)
print_nodes(nodes, n)
