#coding:utf-8
#1_7_B
class Node():
    def __init__(self, node_id):
        self.node_id    =   node_id
        self.parent     =   -1
        self.sibling    =   -1
        self.degree     =   0
        self.depth      =   0
        self.height     =   0
        self.typ        =   'root'
        self.children   =   []

    def set_parent(self, child):
        child.parent = self.node_id
        self.degree += 1
        self.children.append(child)

        if child.degree:
            child.typ = 'internal node'
        else:
            child.typ = 'leaf'

        if self.parent != -1:
            self.typ = 'internal node'

    def set_sibling(self, sibling):
        self.sibling = sibling

def set_depth(tree):
    for node in tree:
        if node.typ == 'root':
            root = node
            break
    queue = []
    queue.extend(root.children)
    while queue:
        node = queue.pop(0)
        node.depth = tree[node.parent].depth + 1
        queue.extend(node.children)

def set_height(tree):
    queue = []
    for node in tree:
        if node.typ == 'leaf':
            queue.append(node)
    while queue:
        leaf = queue.pop(0)
        if leaf.parent != -1 and tree[leaf.parent].height < leaf.height + 1:
            tree[leaf.parent].height = leaf.height + 1
            queue.append(tree[leaf.parent])

n = int(input())
tree = [Node(i) for i in range(n)]

for i in range(n):
    node_id, left, right = map(int, input().split())
    if left != -1:
        tree[node_id].set_parent(tree[left])
        tree[left].set_sibling(right)
    if right != -1:
        tree[node_id].set_parent(tree[right])
        tree[right].set_sibling(left)

set_depth(tree)
set_height(tree)

for node in tree:
    print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(node.node_id, node.parent, node.sibling, node.degree, node.depth, node.height, node.typ))